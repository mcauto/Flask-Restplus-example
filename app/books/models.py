from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields
from marshmallow import validate

from app.api.database import db
from app.api.database import CRUD

class Books(db.Model, CRUD):
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    creation_time = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    is_rent = db.Column(db.Boolean, default=True, nullable=False)
    
    def __init__(self, name, is_rent):
        self.name = name
        self.is_rent = is_rent

class BooksSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')
    id = fields.Integer(dump_only=True)
    name = fields.String(validate=not_blank)
    is_rent = fields.Boolean()
    #self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/api/books"
        else:
            self_link = "/api/books/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'books'