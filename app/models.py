from app import db
import datetime

class CorePlant(db.Model):
    __tablename__ = 'core_plants'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    zone = db.Column(db.String(10), nullable=False)
    plant_family = db.Column(db.String(50), nullable=False)
    created_at = db.Column(
      db.DateTime,
      default=datetime.datetime.now(),
      nullable=False
    )

    def __init__(self, name: str, zone: str, plant_family: int):
        self.name = name
        self.zone = zone
        self.plant_family = plant_family

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'zone': self.zone,
            'plant_family': self.plant_family,
            'created_at': self.created_at
        }

class CompanionPlant(db.Model):
    __tablename__ = 'companion_plants'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    zone = db.Column(db.String(10), nullable=False)
    insect_modifier = db.Column(db.Integer, nullable=False)
    soil_modifier = db.Column(db.Integer, nullable=False)
    flower_modifier = db.Column(db.Integer, nullable=False)
    shade_modifier = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
      db.DateTime,
      default=datetime.datetime.now(),
      nullable=False
    )

    def __init__(self, name: str, zone: str, insect_modifier: int, soil_modifier: int, flower_modifier: int, shade_modifier: int ):
        self.name = name
        self.zone = zone
        self.insect_modifier = insect_modifier
        self.soil_modifier = soil_modifier
        self.flower_modifier = flower_modifier
        self.shade_modifier = shade_modifier

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'zone': self.zone,
            'insect_modifier': self.insect_modifier,
            'soil_modifier': self.soil_modifier,
            'flower_modifier': self.flower_modifier,
            'shade_modifier': self.shade_modifier,
            'created_at': self.created_at
        }

class CoreCompanionPlantMap(db.Model):
    __tablename__ = 'core_companion_plant_mappings'
    id = db.Column(db.Integer, primary_key=True)
    core_plant_id = db.Column(db.Integer, db.ForeignKey('core_plants.id'), nullable=False)
    companion_plant_id = db.Column(db.Integer, db.ForeignKey('companion_plants.id'), nullable=False)
    created_at = db.Column(
      db.DateTime,
      default=datetime.datetime.now(),
      nullable=False
    )

    core_plants = db.relationship('CorePlant', backref=db.backref('core_children', lazy=True))
    companion_plants = db.relationship('CompanionPlant', backref=db.backref('companion_children', lazy=True))

    def __init__(self, core_plant_id: int, companion_plant_id: int):
        self.core_plant_id = core_plant_id
        self.companion_plant_id = companion_plant_id

    def serialize(self):
        return {
            'id': self.id,
            'core_plant_id': self.core_plant_id,
            'companion_plant_id': self.companion_plant_id,
            'created_at': self.created_at,
        }