from flask_caching import Cache
from flask import Blueprint

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache_bp = Blueprint('cache', __name__)

from . import routes