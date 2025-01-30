from flask_caching import Cache

cache = Cache()

def init_cache(app):
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})

from flask import Blueprint

cache_bp = Blueprint('cache', __name__)

from . import routes