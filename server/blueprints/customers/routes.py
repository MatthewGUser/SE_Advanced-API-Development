from flask import Blueprint, request, jsonify
from server.db import db
from server.models import Customer

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers', methods=['GET'])
def get_customers():
    try:
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        
        pagination = Customer.query.paginate(
            page=page,
            per_page=limit,
            error_out=False
        )
        
        return jsonify({
            'customers': [customer.to_dict() for customer in pagination.items],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customers_bp.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:
        customer = Customer.query.get(customer_id)
        
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404
            
        return jsonify(customer.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customers_bp.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        
        if not all(k in data for k in ['name', 'email', 'password']):
            return jsonify({'error': 'Missing required fields'}), 400
            
        if Customer.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already registered'}), 400
            
        customer = Customer(
            name=data['name'],
            email=data['email']
        )
        customer.set_password(data['password'])
        
        try:
            db.session.add(customer)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise
        
        return jsonify(customer.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@customers_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)
        
        try:
            db.session.delete(customer)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise
        
        return jsonify({'message': f'Customer with ID {customer_id} deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
