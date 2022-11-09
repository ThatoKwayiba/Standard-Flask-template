import os
from flask import Flask
from config import Config
from .extensions import db

# Instantiate Celery


# Application Factory
def create_app():
    app = Flask(__name__)

    # Configure the flask app instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')

    app.config.from_object(CONFIG_TYPE)
    # Configure celery
    # celery.conf.update(app.config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # Register blueprints
    register_blueprints(app)
    # Create Session
    return app


# Helper Functions
def register_blueprints(app):
    from .Home import Home_Blueprint
    app.register_blueprint(Home_Blueprint)
