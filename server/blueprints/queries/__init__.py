from flask import Blueprint

queries_bp = Blueprint('queries', __name__)

from . import advanced_queries