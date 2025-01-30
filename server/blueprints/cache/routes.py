from flask import Blueprint, jsonify
from . import cache  # Import cache from __init__.py

cache_bp = Blueprint('cache', __name__)

@cache_bp.route('/cached-route')
@cache.cached(timeout=60)
def cached_route():
    return jsonify({'message': 'This is a cached response'})