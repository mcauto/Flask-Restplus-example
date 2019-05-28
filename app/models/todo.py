from sqlalchemy.sql import text
from marshmallow import Schema
from marshmallow import fields
from marshmallow import validate
from marshmallow import pre_load

from app import db

class Todo(db.Model):
    __tablename__ = "Todo"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(250), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    created = db.Column(db.TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), nullable=False)

    def __init__(self, name, done, **kwargs):
        self.name = name
        self.done = done
        super(Todo, self).__init__(**kwargs)



class TodoSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    done = fields.Boolean()
    created = fields.DateTime(dump_only=True)

    @pre_load
    def make_todos(self, data):
        return Todo(**data)

    class Meta:
        type_ = 'todos'
        fields =("id","name","done","created")
        strict = True