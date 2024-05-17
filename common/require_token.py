from flask import request, jsonify
import jwt
from functools import wraps

key = "test"

def check_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token required!'}), 401
        
        try:
            decoded_token = jwt.decode(token, key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token invalid!'}), 401
        return f(*args, **kwargs)
    return decorated_function