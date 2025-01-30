from flask import Blueprint, jsonify
from .cache import cache

cache_bp = Blueprint('cache', __name__)

@cache_bp.route('/cached-route')
@cache.cached(timeout=60)  # Cache this route for 60 seconds
def cached_route():
    data = {"message": "This is a cached response"}
    return jsonify(data)