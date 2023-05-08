from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_testing import TestCase
from flask_marshmallow import Marshmallow

mongo = MongoEngine()
jwt = JWTManager()
api = Api()
test_client = None
ma = Marshmallow()
