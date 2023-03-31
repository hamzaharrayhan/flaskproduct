from app import db
from app import app
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(250),nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Product {}'.format(self.name)
    
with app.app_context():
    db.create_all()