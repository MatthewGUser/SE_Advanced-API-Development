from flask import Blueprint, request, jsonify
from ...models.inventory import Inventory
from ...db import db, ma

# Create Schema
class InventorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
        load_instance = True
        include_fk = True

inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('', methods=['GET'])
def get_all_inventory():
    try:
        inventory = Inventory.query.all()
        return inventories_schema.dump(inventory)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@inventory_bp.route('/<int:inventory_id>', methods=['GET'])
def get_inventory_item(inventory_id):
    try:
        item = Inventory.query.get_or_404(inventory_id)
        return inventory_schema.dump(item)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@inventory_bp.route('', methods=['POST'])
def add_inventory_item():
    try:
        data = request.get_json()
        item = inventory_schema.load(data)
        db.session.add(item)
        db.session.commit()
        return inventory_schema.dump(item), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@inventory_bp.route('/<int:inventory_id>', methods=['PUT'])
def update_inventory_item(inventory_id):
    try:
        item = Inventory.query.get_or_404(inventory_id)
        data = request.get_json()
        updated_item = inventory_schema.load(data, instance=item, partial=True)
        db.session.commit()
        return inventory_schema.dump(updated_item)
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