from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)



    # Setting up app configuration
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .request import configure_request
    configure_request(app)

    return app
