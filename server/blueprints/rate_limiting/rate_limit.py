from flask import Blueprint, jsonify
from . import limiter

rate_limit_bp = Blueprint('rate_limit', __name__)

@rate_limit_bp.route('/limited-route')
@limiter.limit("5 per minute")
def limited_route():
    return jsonify({"message": "This is a rate-limited response"})