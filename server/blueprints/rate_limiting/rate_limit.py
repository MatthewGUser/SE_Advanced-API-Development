from flask import Blueprint, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

rate_limit_bp = Blueprint('rate_limit', __name__)

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@rate_limit_bp.route('/rate-limited-endpoint', methods=['GET'])
@limiter.limit("5 per minute")
def rate_limited_test():
    return jsonify({
        'message': 'This is a rate-limited endpoint',
        'status': 'success'
    })