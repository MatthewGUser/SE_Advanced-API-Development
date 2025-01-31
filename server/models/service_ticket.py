from server.db import db, service_ticket_mechanic, ticket_parts

class ServiceTicket(db.Model):
    __tablename__ = 'service_ticket'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='pending')
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    
    # Relationships
    customer = db.relationship('Customer', back_populates='tickets')
    mechanics = db.relationship('Mechanic', secondary=service_ticket_mechanic, back_populates='tickets')
    parts = db.relationship('Inventory', secondary=ticket_parts, backref='tickets')

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'customer_id': self.customer_id,
            'mechanics': [{'id': m.id, 'name': m.name} for m in self.mechanics],
            'parts': [{'id': p.id, 'name': p.name, 'price': p.price} for p in self.parts]
        }