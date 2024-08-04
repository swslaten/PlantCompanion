from flask import Blueprint, jsonify, abort, request
from ..models import CoreCompanionPlantMap, db

bp = Blueprint('core_companion_plant_mappings', __name__, url_prefix='/plantmaps')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    core_companion_plant_map = CoreCompanionPlantMap.query.all() # ORM performs SELECT query
    result = []
    for plant in core_companion_plant_map:
        result.append(plant.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

@bp.route('', methods=['POST'])
def create():
    json_data = request.json
    # req body must contain user_id and content
    if 'core_plant_id' not in json_data or 'companion_plant_id' not in json_data:
        return abort(400)
    # construct User
    new_plant_map = CoreCompanionPlantMap(
        core_plant_id = json_data['core_plant_id'],
        companion_plant_id = json_data['companion_plant_id'],
    )
    db.session.add(new_plant_map) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(new_plant_map.serialize())

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    selected_plant = CoreCompanionPlantMap.query.get_or_404(id)
    return jsonify(selected_plant.serialize())