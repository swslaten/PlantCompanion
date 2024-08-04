from flask import Blueprint, jsonify, abort, request
from ..models import CompanionPlant, db

bp = Blueprint('companion_plants', __name__, url_prefix='/companionplants')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    companion_plants = CompanionPlant.query.all() # ORM performs SELECT query
    result = []
    for plant in companion_plants:
        result.append(plant.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

@bp.route('', methods=['POST'])
def create():
    json_data = request.json
    # req body must contain user_id and content
    if 'name' not in json_data or 'zone' not in json_data or 'insect_modifier' not in json_data:
        return abort(400)
    
    if 'insect_modifier' not in json_data or 'soil_modifier' not in json_data or 'flower_modifier' not in json_data or 'shade_modifier' not in json_data:
        return abort(400)
    
    # construct User
    new_companion_plant = CompanionPlant(
        name = json_data['name'],
        zone = json_data['zone'],
        insect_modifier = json_data['insect_modifier'],
        soil_modifier = json_data['soil_modifier'],
        flower_modifier = json_data['flower_modifier'],
        shade_modifier = json_data['shade_modifier']
    )
    db.session.add(new_companion_plant) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(new_companion_plant.serialize())

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    selected_plant = CompanionPlant.query.get_or_404(id)
    return jsonify(selected_plant.serialize())