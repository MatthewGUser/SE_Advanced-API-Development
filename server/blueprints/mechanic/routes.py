from flask import Blueprint, request, jsonify
from server.models.mechanic import Mechanic
from server.models.service_ticket import ServiceTicket
from server.db import db
from sqlalchemy import func

mechanic_bp = Blueprint('mechanic', __name__)

@mechanic_bp.route('/mechanics', methods=['GET'])
def get_mechanics():
    mechanics = Mechanic.query.all()
    return jsonify([mechanic.to_dict() for mechanic in mechanics])

@mechanic_bp.route('/mechanics/top', methods=['GET'])
def get_top_mechanics():
    top_mechanics = db.session.query(
        Mechanic,
        func.count(ServiceTicket.id).label('ticket_count')
    ).join(
        ServiceTicket.mechanics
    ).group_by(
        Mechanic.id
    ).order_by(
        func.count(ServiceTicket.id).desc()
    ).all()
    
    return jsonify([{
        **mechanic.to_dict(),
        'ticket_count': count
    } for mechanic, count in top_mechanics])

@mechanic_bp.route('/mechanics', methods=['POST'])
def create_mechanic():
    data = request.get_json()
    mechanic = Mechanic(name=data['name'])
    db.session.add(mechanic)
    db.session.commit()
    return jsonify(mechanic.to_dict()), 201