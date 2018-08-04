from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(128))
    admin = db.Column(db.Boolean)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return 'Пользователь {}'.format(self.name)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(11), index=True, unique=True)
    comment = db.Column(db.String(64))
    operations = db.relationship('Operation', backref='operation', lazy='dynamic' )
    def __repr__(self):
        return 'Клиент {}'.format(self.phone)

class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    vid_op = db.Column(db.Integer, db.ForeignKey('vid_op.id'))
    sum = db.Column(db.Float)
    bonus = db.Column(db.Float)

class Vid_op(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazv = db.Column(db.String(28))