from flask import Blueprint

rate_limit_bp = Blueprint('rate_limit', __name__)

from . import rate_limit