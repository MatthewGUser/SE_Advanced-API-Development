from flask import Flask
from flask_migrate import Migrate
from .config import config
from .db import db, ma
from .blueprints.cache import cache, init_cache

def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)
    init_cache(app)  # Initialize cache before blueprints

    with app.app_context():
        from .models import Customer, Inventory, ServiceTicket, Mechanic
        
    from .blueprints import init_app as init_blueprints
    init_blueprints(app)
    
    return app