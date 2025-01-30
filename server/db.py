from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Association tables
service_ticket_mechanic = db.Table(
    'service_ticket_mechanic',
    db.Column('service_ticket_id', db.Integer, db.ForeignKey('service_ticket.id')),
    db.Column('mechanic_id', db.Integer, db.ForeignKey('mechanic.id')),
    extend_existing=True
)

ticket_parts = db.Table(
    'ticket_parts',
    db.Column('ticket_id', db.Integer, db.ForeignKey('service_ticket.id')),
    db.Column('part_id', db.Integer, db.ForeignKey('inventory.id')),
    extend_existing=True
)