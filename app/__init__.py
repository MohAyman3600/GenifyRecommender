from configparser import ConfigParser
import logging.config
from flask import Flask
from flask import Blueprint
from flask_restx import Api
from .extensions import mongo, jwt, api, ma
from .config.config import config_by_name



def setup_logging(config_file_path):
    config_parser = ConfigParser()
    config_parser.read(config_file_path)
    logging.config.fileConfig(config_parser)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    # Initialize Flask-JWT-Extended
    jwt.init_app(app)

    # Initialize MongoDB
    mongo.init_app(app)

    # Initialize Marshmallow
    ma.init_app(app)

   # load logging configuration from file
    setup_logging('logging_config.ini')

    # Initialize Flask-RESTX API
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api = Api(blueprint, title='ML API', version='1.0', description='API for machine learning model')
    app.register_blueprint(blueprint)

    # Import and add namespaces
    from app.api.resources import auth_ns, user_ns, pred_ns
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(pred_ns)

    # Add Swagger UI endpoint
    @app.route('/swagger-ui/')
    def swagger_ui():
        return app.send_static_file('swagger-ui.html')
    
    return app
