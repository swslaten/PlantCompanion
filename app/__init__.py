# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Check for this line and make sure 'config' module is not being imported
    # from config import Config
    # app.config.from_object(Config)  # This line should be removed or updated

    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin123@db:5432/plantcompanion',
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    db.init_app(app)

    # Import and register routes
    from .api import core_plants, companion_plants, core_companion_plant_map
    app.register_blueprint(core_plants.bp)
    app.register_blueprint(companion_plants.bp)
    app.register_blueprint(core_companion_plant_map.bp)

    return app
