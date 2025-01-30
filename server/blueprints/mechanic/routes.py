from flask import Blueprint, request, jsonify
from server.models.mechanic import Mechanic
from server.db import db

mechanic_bp = Blueprint('mechanic', __name__)

@mechanic_bp.route('/', methods=['POST'])
def create_mechanic():
    data = request.get_json()
    mechanic = Mechanic(name=data['name'])
    db.session.add(mechanic)
    db.session.commit()
    return jsonify(mechanic.to_dict()), 201

@mechanic_bp.route('/<int:id>', methods=['GET'])
def get_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    return jsonify(mechanic.to_dict())

@mechanic_bp.route('/<int:id>', methods=['PUT'])
def update_mechanic(id):
    data = request.get_json()
    mechanic = Mechanic.query.get_or_404(id)
    mechanic.name = data['name']
    db.session.commit()
    return jsonify(mechanic.to_dict())

@mechanic_bp.route('/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    db.session.delete(mechanic)
    db.session.commit()
    return '', 204