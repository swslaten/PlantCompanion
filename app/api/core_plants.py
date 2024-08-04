from flask import Blueprint, jsonify, abort, request
from ..models import CorePlant, db

bp = Blueprint('core_plants', __name__, url_prefix='/coreplants')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    core_plants = CorePlant.query.all() # ORM performs SELECT query
    result = []
    for plant in core_plants:
        result.append(plant.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

@bp.route('', methods=['POST'])
def create():
    json_data = request.json
    # req body must contain user_id and content
    if 'name' not in json_data or 'zone' not in json_data or 'plant_family' not in json_data:
        return abort(400)

    # construct User
    new_core_plant = CorePlant(
        name = json_data['name'],
        zone = json_data['zone'],
        plant_family = json_data['plant_family']
    )
    db.session.add(new_core_plant) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(new_core_plant.serialize())

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    
    selected_plant = CorePlant.query.get_or_404(id)
    return jsonify(selected_plant.serialize())