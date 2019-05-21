from sqlalchemy.sql import text
from marshmallow import Schema
from marshmallow import fields
from marshmallow import validate

from app.database import db

class Todo(db.Model):
    __tablename__ = "Todo"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(250), nullable=False)
    created = db.Column(db.TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

class TodoSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    created = fields.DateTime(0)
    done = fields.Boolean()

    class Meta:
        type_ = 'todos'
        strict = True