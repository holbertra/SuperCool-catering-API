from . import db
from  datetime import datetime

from marshmallow import Schema, fields

class Event(db.Model):
    __tablename__ = 'events' 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)  
    menu_choice = db.Column(db.Integer, default=1)
    ev_date = db.Column(db.DateTime)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id')) #Foreign Key
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)    

    def __init__(self, title, menu_choice, ev_date, client_id, date_created, last_modified):
        self.title = title
        self.menu_choice = menu_choice
        self.ev_date = ev_date
        self.client_id = client_id
        self.datetime = date_created
        self.last_modified = last_modified

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, old, data):
        for key, item in data.items():
            setattr(old, key, item)
        self.last_modified = datetime.utcnow()
        db.session.commit()
        return old

    @staticmethod
    def get_one_event(evnt_id):
        print(f'Enter get_one_event({evnt_id})')
        return Event.query.filter_by(id=evnt_id).first()  

    @staticmethod
    def get_all_events():
        return Event.query.all()         

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    ev_title = fields.Str(required=True)
    menu_option = fields.Int(dump_only=True)
    date = fields.DateTime(dum_only=True)
    client_id = fields.Str(required=True)      # Foreign Key field
    date_created = fields.DateTime(dum_only=True)
    last_modified = fields.DateTime(dump_only=True)