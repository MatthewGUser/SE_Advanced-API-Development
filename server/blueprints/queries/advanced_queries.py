from flask import Blueprint, jsonify, request
from server.models.customer import Customer
from server.models.mechanic import Mechanic
from server.models.service_ticket import ServiceTicket
from server.db import db
from sqlalchemy import func

queries_bp = Blueprint('queries', __name__)

@queries_bp.route('/customers', methods=['GET'])
def get_customers_paginated():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    customers = Customer.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    
    return jsonify({
        'customers': [customer.to_dict() for customer in customers.items],
        'total': customers.total,
        'pages': customers.pages,
        'current_page': customers.page
    })

@queries_bp.route('/mechanics', methods=['GET'])
def get_mechanics_by_tickets():
    mechanics = db.session.query(
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
    } for mechanic, count in mechanics])