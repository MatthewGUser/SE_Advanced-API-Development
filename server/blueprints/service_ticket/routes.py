from flask import jsonify, request
from . import service_ticket_bp
from ...models.service_ticket import ServiceTicket
from ...models.mechanic import Mechanic
from ...models.inventory import Inventory
from ...db import db, ma
from ..auth.tokens import token_required

class ServiceTicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTicket
        include_fk = True

ticket_schema = ServiceTicketSchema()
tickets_schema = ServiceTicketSchema(many=True)

@service_ticket_bp.route('/my-tickets', methods=['GET'])
@token_required
def get_my_tickets(customer_id):
    tickets = ServiceTicket.query.filter_by(customer_id=customer_id).all()
    return tickets_schema.dump(tickets)

@service_ticket_bp.route('', methods=['POST'])
@token_required
def create_ticket(customer_id):
    data = request.get_json()
    
    new_ticket = ServiceTicket(
        description=data['description'],
        customer_id=customer_id,
        status='pending'
    )
    
    if 'mechanic_ids' in data:
        mechanics = Mechanic.query.filter(Mechanic.id.in_(data['mechanic_ids'])).all()
        new_ticket.mechanics = mechanics
    
    db.session.add(new_ticket)
    db.session.commit()
    
    return ticket_schema.dump(new_ticket), 201

@service_ticket_bp.route('/<int:ticket_id>/edit', methods=['PUT'])
@token_required
def edit_ticket_mechanics(customer_id, ticket_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    data = request.get_json()
    
    if 'remove_ids' in data:
        mechanics_to_remove = Mechanic.query.filter(Mechanic.id.in_(data['remove_ids'])).all()
        for mechanic in mechanics_to_remove:
            ticket.mechanics.remove(mechanic)
            
    if 'add_ids' in data:
        mechanics_to_add = Mechanic.query.filter(Mechanic.id.in_(data['add_ids'])).all()
        for mechanic in mechanics_to_add:
            ticket.mechanics.append(mechanic)
    
    db.session.commit()
    return ticket_schema.dump(ticket)

@service_ticket_bp.route('/<int:ticket_id>/status', methods=['PATCH'])
@token_required
def update_ticket_status(customer_id, ticket_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    data = request.get_json()
    
    if 'status' in data and data['status'] in ['pending', 'in_progress', 'completed']:
        ticket.status = data['status']
        db.session.commit()
        return ticket_schema.dump(ticket)
    
    return jsonify({'message': 'Invalid status'}), 400

@service_ticket_bp.route('/<int:ticket_id>/add-part', methods=['POST'])
@token_required
def add_part_to_ticket(customer_id, ticket_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    data = request.get_json()
    
    if 'part_id' in data:
        part = Inventory.query.get_or_404(data['part_id'])
        ticket.parts.append(part)
        db.session.commit()
        return ticket_schema.dump(ticket)
    
    return jsonify({'message': 'Part ID required'}), 400

@service_ticket_bp.route('/<int:ticket_id>', methods=['DELETE'])
@token_required
def delete_ticket(customer_id, ticket_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    
    if ticket.customer_id != customer_id:
        return jsonify({'message': 'Unauthorized'}), 403
        
    db.session.delete(ticket)
    db.session.commit()
    return '', 204