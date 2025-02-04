from flask import Blueprint

# Import blueprints
from .auth.routes import auth_bp
from .cache.routes import cache_bp
from .customers.routes import customers_bp 
from .inventory.routes import inventory_bp
from .queries.advanced_queries import queries_bp
from .rate_limiting.rate_limit import rate_limit_bp
from .service_ticket.routes import service_ticket_bp
from .mechanic.routes import mechanic_bp

def init_app(app):
    """Register all blueprints with the Flask app"""
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(cache_bp, url_prefix='/cache')
    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    app.register_blueprint(queries_bp, url_prefix='/queries')
    app.register_blueprint(rate_limit_bp)  # No prefix - applies globally
    app.register_blueprint(service_ticket_bp, url_prefix='/service_tickets')
    app.register_blueprint(mechanic_bp, url_prefix='/mechanics')
    return app