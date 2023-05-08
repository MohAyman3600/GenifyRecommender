from datetime import timedelta
from flask import request
from flask_restx import Namespace, Resource, fields, abort
from flask_bcrypt import check_password_hash
from flask_jwt_extended import create_access_token

from app.extensions import jwt
from app.api.models import User


auth_ns = Namespace('auth', description='Authentication operations')

login_request = auth_ns.model('LoginRequest', {
    'email': fields.String(required=True, description='The user\'s email'),
    'password': fields.String(required=True, description='The user\'s password')
})

login_response = auth_ns.model('LoginResponse', {
    'access_token': fields.String(description='The access token for the authenticated user')
})


@auth_ns.route('/login')
class LoginResource(Resource):
    """Login to obtain the authentication access token"""

    @auth_ns.expect(login_request)
    @auth_ns.marshal_with(login_response, code=200)
    def post(self):
        try:
            data = request.json

            email = data.get('email')
            password = data.get('password')

            user = User.objects(email=email).first()

            if not user or not check_password_hash(user.password, password):
                abort(401, 'Invalid email or password')

            # Add an expiry time of 1 hour to the access token
            expires_delta = timedelta(days=10)
            access_token = create_access_token(identity=str(user.id))

            return {'access_token': access_token}

        except Exception as e:
            auth_ns.logger.error(f"Error while logging in: {str(e)}")
            abort(500, 'An error occurred while logging in')
