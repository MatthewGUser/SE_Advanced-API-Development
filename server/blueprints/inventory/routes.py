from flask import Blueprint, request, jsonify
from server.models.inventory import Inventory
from server.db import db

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/', methods=['POST'])
def create_inventory():
    data = request.get_json()
    part = Inventory(name=data['name'], price=data['price'])
    db.session.add(part)
    db.session.commit()
    return jsonify(part.to_dict()), 201

@inventory_bp.route('/<int:id>', methods=['GET'])
def get_inventory(id):
    part = Inventory.query.get_or_404(id)
    return jsonify(part.to_dict())