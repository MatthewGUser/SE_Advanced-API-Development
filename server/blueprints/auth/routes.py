from flask import Blueprint, request, jsonify
from .tokens import encode_token
from server.models.customer import Customer
from server.db import db
from . import auth_bp

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    customer = Customer.query.filter_by(email=email).first()
    if customer and customer.password == password:
        token = encode_token(customer.id)
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401