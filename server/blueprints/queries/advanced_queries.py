from flask import Blueprint, request, jsonify
from server.models.customer import Customer

queries_bp = Blueprint('queries', __name__)

@queries_bp.route('/customers', methods=['GET'])
def get_customers():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    customers = Customer.query.paginate(page, per_page, False)
    return jsonify([customer.to_dict() for customer in customers.items])