from functools import wraps
from flask import request, current_app, jsonify

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            parts = request.headers['Authorization'].split()
            if len(parts) == 2 and parts[0] == 'Bearer':
                token = parts[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        if token != current_app.config['AUTH_TOKEN']:
            return jsonify({'message': 'Invalid token!'}), 401

        return func(*args, **kwargs)

    return decorated
