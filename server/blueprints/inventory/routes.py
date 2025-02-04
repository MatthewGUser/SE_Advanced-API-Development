from flask import Blueprint, request, jsonify
from server.models.inventory import Inventory
from server.db import db

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('', methods=['GET'])
def get_all_inventory():
    try:
        inventory = Inventory.query.all()
        return jsonify([item.to_dict() for item in inventory])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@inventory_bp.route('/<int:inventory_id>', methods=['GET'])
def get_inventory_item(inventory_id):
    try:
        item = Inventory.query.get_or_404(inventory_id)
        return jsonify(item.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@inventory_bp.route('', methods=['POST'])
def add_inventory_item():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not all(k in data for k in ['name', 'price']):
            return jsonify({'error': 'Missing required fields'}), 400
            
        item = Inventory(
            name=data['name'],
            price=data['price']
        )
        db.session.add(item)
        db.session.commit()
        return jsonify(item.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@inventory_bp.route('/<int:inventory_id>', methods=['PUT'])
def update_inventory_item(inventory_id):
    try:
        item = Inventory.query.get_or_404(inventory_id)
        data = request.get_json()
        
        if 'name' in data:
            item.name = data['name']
        if 'price' in data:
            item.price = data['price']
            
        db.session.commit()
        return jsonify(item.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@inventory_bp.route('/<int:inventory_id>', methods=['DELETE'])
def delete_inventory_item(inventory_id):
    try:
        item = Inventory.query.get_or_404(inventory_id)
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500