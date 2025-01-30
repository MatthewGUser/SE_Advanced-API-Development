from server.db import db, service_ticket_mechanic

class Mechanic(db.Model):
    __tablename__ = 'mechanic'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    tickets = db.relationship(
        'ServiceTicket',
        secondary=service_ticket_mechanic,
        back_populates='mechanics'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ticket_count': len(self.tickets) if self.tickets else 0
        }