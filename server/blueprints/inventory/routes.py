from flask import Blueprint, request, jsonify
from server.models.inventory import Inventory
from server.db import db

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/inventory', methods=['GET'])
def get_all_inventory():
    inventory = Inventory.query.all()
    return jsonify([item.to_dict() for item in inventory])

@inventory_bp.route('/inventory/<int:inventory_id>', methods=['GET'])
def get_inventory_item(inventory_id):
    item = Inventory.query.get_or_404(inventory_id)
    return jsonify(item.to_dict())

@inventory_bp.route('/inventory', methods=['POST'])
def add_inventory_item():
    data = request.get_json()
    item = Inventory(
        name=data['name'],
        price=data['price']
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@inventory_bp.route('/inventory/<int:inventory_id>', methods=['PUT'])
def update_inventory_item(inventory_id):
    data = request.get_json()
    item = Inventory.query.get_or_404(inventory_id)
    item.name = data.get('name', item.name)
    item.price = data.get('price', item.price)
    db.session.commit()
    return jsonify(item.to_dict())

@inventory_bp.route('/inventory/<int:inventory_id>', methods=['DELETE'])
def remove_inventory_item(inventory_id):
    item = Inventory.query.get_or_404(inventory_id)
    db.session.delete(item)
    db.session.commit()
    return '', 204