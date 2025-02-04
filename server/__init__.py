from flask import Flask
from flask_migrate import Migrate
from .config import config
from .db import db, ma 
from .blueprints.cache import cache, init_cache
from .blueprints import init_app as init_blueprints

def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    init_cache(app)

    with app.app_context():
        from .models import Customer, Inventory, ServiceTicket, Mechanic
        
    # Register blueprints using the centralized registration function
    init_blueprints(app)
    
    return app