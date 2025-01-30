from server.db import db

class ServiceTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    # Add other fields as necessary

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'customer_id': self.customer_id,
            # Add other fields as necessary
        }