from flask import Blueprint, jsonify
from . import cache

cache_bp = Blueprint('cache', __name__)

@cache_bp.route('/cached-endpoint')
@cache.cached(timeout=60)  # Cache for 60 seconds
def cached_test():
    return jsonify({
        'message': 'This is a cached response',
        'status': 'success'
    })