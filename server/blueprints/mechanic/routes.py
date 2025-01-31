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
    try:
        # Query top mechanics including those with no tickets
        top_mechanics = db.session.query(
            Mechanic,
            func.count(ServiceTicket.id).label('ticket_count')
        ).outerjoin(
            ServiceTicket.mechanics
        ).group_by(
            Mechanic.id
        ).order_by(
            func.count(ServiceTicket.id).desc()
        ).limit(5).all()
        
        # Format response
        response = [{
            'id': mechanic.id,
            'name': mechanic.name,
            'ticket_count': count
        } for mechanic, count in top_mechanics]
        
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@mechanic_bp.route('/mechanics', methods=['POST'])
def create_mechanic():
    data = request.get_json()
    mechanic = Mechanic(name=data['name'])
    db.session.add(mechanic)
    db.session.commit()
    return jsonify(mechanic.to_dict()), 201


@mechanic_bp.route('/mechanics/<int:mechanic_id>', methods=['DELETE'])
def delete_mechanic(mechanic_id):
    try:
        mechanic = Mechanic.query.get_or_404(mechanic_id)
        
        try:
            db.session.delete(mechanic)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise
        
        return jsonify({'message': f'Mechanic with ID {mechanic_id} deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500