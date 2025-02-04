from flask import Blueprint
from flask_caching import Cache

cache = Cache(config={
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 300
})

cache_bp = Blueprint('cache', __name__)

def init_cache(app):
    cache.init_app(app)

from . import routes