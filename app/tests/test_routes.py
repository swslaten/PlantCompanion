import pytest
from app import create_app, db
from ..models import CorePlant, CompanionPlant, CoreCompanionPlantMap

@pytest.fixture
def app():
    app = create_app()  # Adjust this according to your app factory

    app.config.update({
    "TESTING": True,
    "SQLALCHEMY_DATABASE_URI": 'sqlite:///:memory:'
    })  

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_coreplants_get_all(client):
    
    test_core_plant = CorePlant(name="Tomato",zone="123",plant_family="Nightshade")

    db.session.add(test_core_plant)
    db.session.commit()

    # Get response data
    response = client.get('/coreplants')
    
    # Check the status code
    assert response.status_code == 200
    
    # Check the response data
    json_data = response.get_json()[0]

    # Check that the proper keys are present in the response
    required_keys = {"name","zone","plant_family"}
    assert required_keys.issubset(json_data.keys())

    # Check to ensure the data is obtained correctly 
    assert json_data["name"] == "Tomato"
    assert json_data["zone"] == "123"
    assert json_data["plant_family"] == "Nightshade"

def test_companionplants_get_all(client):
    
    test_companion_plant = CompanionPlant(name="Negi",zone="123",insect_modifier="1",soil_modifier="2",flower_modifier="3",shade_modifier="6")

    db.session.add(test_companion_plant)
    db.session.commit()

    # Get response data
    response = client.get('/companionplants')
    
    # Check the status code
    assert response.status_code == 200
    
    # Check the response data
    json_data = response.get_json()[0]

    # Check that the proper keys are present in the response
    required_keys = {"name","zone","insect_modifier","soil_modifier","flower_modifier","shade_modifier"}
    assert required_keys.issubset(json_data.keys())

    # Check to ensure the data is obtained correctly 
    assert json_data["name"] == "Negi"
    assert json_data["zone"] == "123"
    assert json_data["insect_modifier"] == 1
    assert json_data["soil_modifier"] == 2
    assert json_data["flower_modifier"] == 3
    assert json_data["shade_modifier"] == 6

def test_plant_mappings(client):
    
    test_plant_mapping = CoreCompanionPlantMap(core_plant_id="1",companion_plant_id="2")

    db.session.add(test_plant_mapping)
    db.session.commit()

    # Get response data
    response = client.get('/plantmaps')
    
    # Check the status code
    assert response.status_code == 200
    
    # Check the response data
    json_data = response.get_json()[0]

    # Check that the proper keys are present in the response
    required_keys = {"core_plant_id","companion_plant_id"}
    assert required_keys.issubset(json_data.keys())

    # Check to ensure the data is obtained correctly 
    assert json_data["core_plant_id"] == 1
    assert json_data["companion_plant_id"] == 2

