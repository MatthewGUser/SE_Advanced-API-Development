from flask import Blueprint, request, jsonify
from server.models.service_ticket import ServiceTicket
from server.models.inventory import Inventory
from server.models.mechanic import Mechanic
from server.db import db
from server.blueprints.auth.tokens import token_required

service_ticket_bp = Blueprint('service_ticket', __name__)

# Root level route for my-tickets
@service_ticket_bp.route('/my-tickets', methods=['GET'])
@token_required
def get_my_tickets(customer_id):
    try:
        # Verify customer_id from token
        if not customer_id:
            return jsonify({'error': 'Not authenticated'}), 401
            
        # Get only tickets for this customer
        tickets = ServiceTicket.query.filter_by(customer_id=customer_id).all()
        
        return jsonify({
            'tickets': [ticket.to_dict() for ticket in tickets],
            'count': len(tickets),
            'customer_id': customer_id
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@service_ticket_bp.route('/service_tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    try:
        # Get specific ticket by ID
        ticket = ServiceTicket.query.get_or_404(ticket_id)
        return jsonify(ticket.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@service_ticket_bp.route('/service_tickets', methods=['POST'])
@token_required
def create_ticket(customer_id):
    try:
        data = request.get_json()
        
        # Validate required fields
        if 'description' not in data:
            return jsonify({'error': 'Description is required'}), 400
            
        # Create ticket
        ticket = ServiceTicket(
            description=data['description'],
            customer_id=customer_id
        )
        
        # Add mechanics if provided
        if 'mechanic_ids' in data:
            mechanics = Mechanic.query.filter(Mechanic.id.in_(data['mechanic_ids'])).all()
            ticket.mechanics = mechanics
            
        db.session.add(ticket)
        db.session.commit()
        
        return jsonify(ticket.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@service_ticket_bp.route('/service_tickets/<int:ticket_id>/add-part', methods=['POST'])
@token_required
def add_part_to_ticket(customer_id, ticket_id):
    try:
        data = request.get_json()
        
        if 'part_id' not in data:
            return jsonify({'error': 'Missing part_id field'}), 400
            
        # Get ticket and verify ownership
        ticket = ServiceTicket.query.get_or_404(ticket_id)
        if ticket.customer_id != customer_id:
            return jsonify({'error': 'Not authorized to modify this ticket'}), 403
            
        # Get part
        part = Inventory.query.get_or_404(data['part_id'])
        
        # Add part to ticket
        ticket.parts.append(part)
        db.session.commit()
        
        return jsonify(ticket.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@service_ticket_bp.route('/service_tickets/<int:ticket_id>/edit', methods=['PUT'])
@token_required
def edit_ticket(customer_id, ticket_id):
    data = request.get_json()
    remove_ids = data.get('remove_ids', [])
    add_ids = data.get('add_ids', [])
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    if ticket.customer_id != customer_id:
        return jsonify({'message': 'Unauthorized'}), 403
    for mechanic_id in remove_ids:
        mechanic = Mechanic.query.get(mechanic_id)
        if mechanic in ticket.mechanics:
            ticket.mechanics.remove(mechanic)
    for mechanic_id in add_ids:
        mechanic = Mechanic.query.get(mechanic_id)
        if mechanic not in ticket.mechanics:
            ticket.mechanics.append(mechanic)
    db.session.commit()
    return jsonify(ticket.to_dict())

@service_ticket_bp.route('/service_tickets/<int:ticket_id>/status', methods=['PATCH'])
@token_required
def update_status(customer_id, ticket_id):
    data = request.get_json()
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    if ticket.customer_id != customer_id:
        return jsonify({'message': 'Unauthorized'}), 403
    ticket.status = data['status']
    db.session.commit()
    return jsonify(ticket.to_dict())

@service_ticket_bp.route('/service_tickets/<int:ticket_id>', methods=['DELETE'])
@token_required
def delete_ticket(customer_id, ticket_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    if ticket.customer_id != customer_id:
        return jsonify({'message': 'Unauthorized'}), 403
    db.session.delete(ticket)
    db.session.commit()
    return '', 204

