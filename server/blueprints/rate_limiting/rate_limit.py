from flask import Blueprint, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

rate_limit_bp = Blueprint('rate_limit', __name__)

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@rate_limit_bp.route('/limited-route')
@limiter.limit("5 per minute")
def limited_route():
    return jsonify({'message': 'This is a rate-limited response'})