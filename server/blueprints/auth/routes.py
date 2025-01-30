from flask import Blueprint, request, jsonify
from server.models.customer import Customer
from server.db import db
from .tokens import encode_token

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        if not data or not all(k in data for k in ['email', 'password']):
            return jsonify({'error': 'Missing email or password'}), 400
            
        email = data.get('email')
        password = data.get('password')
        
        customer = Customer.query.filter_by(email=email).first()
        
        if customer and customer.check_password(password):
            token = encode_token(customer.id)
            return jsonify({
                'token': token,
                'customer': customer.to_dict()
            })
            
        return jsonify({'error': 'Invalid credentials'}), 401
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500