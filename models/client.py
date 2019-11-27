from . import db
import datetime

from marshmallow import Schema, fields

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    def __init__(self, email, password, first_name, last_name=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.date_created = datetime.datetime.now()
        self.last_modified = datetime.datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return 'client successfully created'