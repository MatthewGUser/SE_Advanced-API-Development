from flask_caching import Cache
from flask import Blueprint

cache = Cache()
cache_bp = Blueprint('cache', __name__)

def init_cache(app):
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})

from . import routes