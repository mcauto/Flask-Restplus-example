from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

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