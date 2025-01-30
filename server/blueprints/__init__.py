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
    # Register all blueprints
    app.register_blueprint(auth_bp)  # Remove prefix for base /login
    app.register_blueprint(cache_bp)  # Remove prefix for direct endpoint
    app.register_blueprint(customers_bp)  # URLs already include /customers
    app.register_blueprint(inventory_bp)  # URLs already include /inventory
    app.register_blueprint(mechanic_bp)  # URLs already include /mechanics
    app.register_blueprint(queries_bp)  # For advanced queries
    app.register_blueprint(service_ticket_bp)  # For service tickets
    app.register_blueprint(rate_limit_bp)  # Remove prefix for direct endpoint