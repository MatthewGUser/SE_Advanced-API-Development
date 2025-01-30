from flask import Blueprint

# Import blueprints
from .auth.routes import auth_bp
from .cache.routes import cache_bp
from .inventory.routes import inventory_bp
from .queries.advanced_queries import queries_bp
from .rate_limiting.rate_limit import rate_limit_bp
from .service_ticket.routes import service_ticket_bp

# Initialize blueprints
def init_app(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(cache_bp, url_prefix='/cache')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    app.register_blueprint(queries_bp, url_prefix='/queries')
    app.register_blueprint(rate_limit_bp, url_prefix='/rate_limit')
    app.register_blueprint(service_ticket_bp, url_prefix='/service_ticket')