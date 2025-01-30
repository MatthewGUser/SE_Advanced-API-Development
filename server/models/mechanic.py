from server.db import db

class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    tickets = db.relationship('ServiceTicket', secondary='service_ticket_mechanic', back_populates='mechanics')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

# Association table for many-to-many relationship between ServiceTicket and Mechanic
service_ticket_mechanic = db.Table('service_ticket_mechanic',
    db.Column('service_ticket_id', db.Integer, db.ForeignKey('service_ticket.id'), primary_key=True),
    db.Column('mechanic_id', db.Integer, db.ForeignKey('mechanic.id'), primary_key=True)
)