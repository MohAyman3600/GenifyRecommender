from flask import request
from flask_restx import Namespace, Resource, fields, abort

from app.api.models import User
from app.api.validators import UserSchema

user_ns = Namespace('users', description='User operations')

user_create_request = user_ns.model('UserCreateRequest', {
    'email': fields.String(required=True, description='The user\'s email'),
    'password': fields.String(required=True, description='The user\'s password')
})

user_update_request = user_ns.model('UserUpdateRequest', {
    'email': fields.String(description='The user\'s email'),
    'password': fields.String(description='The user\'s password')
})

user_response = user_ns.model('UserResponse', {
    'id': fields.String(description='The user identifier'),
    'email': fields.String(description='The user\'s email'),
    'date_created': fields.DateTime(description='The user creation datetime')
})


@user_ns.route('/')
class UserListResource(Resource):
    """Resource for creating and retrieving users"""

    @user_ns.expect(user_create_request)
    @user_ns.marshal_with(user_response, code=201)
    def post(self):
        data = request.json

        user_schema = UserSchema()

        try:
            user = User(**data)

            user.hash_password()

            user.save()

            return user_schema.dump(user), 201

        except Exception as e:
            user_ns.logger.error(f'Error creating user: {str(e)}')
            abort(500, f'Failed to create user {str(e)}')

    @user_ns.marshal_list_with(user_response)
    def get(self):
        try:
            users = User.objects.all()
            user_schema = UserSchema(many=True)
            return user_schema.dump(users)

        except Exception as e:
            user_ns.logger.error(f'Error retrieving users: {str(e)}')
            abort(500, 'Failed to retrieve users')


@user_ns.route('/<string:email>')
class UserResource(Resource):
    """Resource for retrieving and updating a single user"""

    @user_ns.marshal_with(user_response)
    def get(self, email):
        try:
            user = User.objects(email=email).first()

            if not user:
                abort(404, 'User not found')

            return user

        except Exception as e:
            user_ns.logger.error(f'Error retrieving user: {str(e)}')
            abort(500, 'Failed to retrieve user')

    @user_ns.expect(user_update_request)
    @user_ns.marshal_with(user_response)
    def put(self, email):
        try:
            user = User.objects(email=email).first()

            if not user:
                abort(404, 'User not found')

            data = request.json

            user_schema = UserSchema()

            errors = user_schema.validate(data, partial=True)

            if errors:
                return {'message': 'Validation errors', 'errors': errors}, 400

            user.update(**data)

            if 'password' in data:
                user.hash_password()

            user.save()

            return user_schema.dump(user)

        except Exception as e:
            user_ns.logger.error(f'Error updating user: {str(e)}')
            abort(500, 'Failed to update user')

    @user_ns.response(204, 'User deleted')
    def delete(self, email):
        try:
            user = User.objects(email=email).first()
            if not user:
                abort(404, f'User with email {email} not found')
            user.delete()
        except Exception as e:
            user_ns.logger.error(f'Error deleting user: {str(e)}')
            abort(500, 'Failed to delete user')
        return '', 204