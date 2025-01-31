import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify, current_app
from server.models.customer import Customer

def encode_token(customer_id):
    """Generate JWT token for customer"""
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': customer_id
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

def decode_token(token):
    """Decode and validate JWT token"""
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'X-Access-Token' in request.headers:
            token = request.headers['X-Access-Token']
        elif 'Authorization' in request.headers:
            auth = request.headers['Authorization']
            token = auth.split(' ')[1] if ' ' in auth else auth
            
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
            
        try:
            customer_id = decode_token(token)
            current_customer = Customer.query.get(customer_id)
            
            if not current_customer:
                return jsonify({'message': 'Invalid token'}), 401
                
            return f(current_customer.id, *args, **kwargs)
            
        except Exception as e:
            return jsonify({'message': 'Token validation failed'}), 401
            
    return decorated