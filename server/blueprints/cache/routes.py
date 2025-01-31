from flask import Blueprint, jsonify
from . import cache

cache_bp = Blueprint('cache', __name__)

@cache_bp.route('/cached-endpoint')
@cache.cached(timeout=60)
def cached_test():
    try:
        return jsonify({
            'message': 'This is a cached response',
            'status': 'success',
            'cache_info': 'Response cached for 60 seconds'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500