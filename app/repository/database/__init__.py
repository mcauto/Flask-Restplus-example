from typing import List, Tuple
from sqlalchemy.sql.elements import ColumnElement 
from flask_sqlalchemy import SQLAlchemy
from app.models.todo import Todo
from app.constants import STATUS_CODE

class TodoRepository(object):
	def __init__(self, db:SQLAlchemy):
		self.db = db
	def get_list(self, filters: ColumnElement)->Tuple[STATUS_CODE, List[Todo]]:
		code = STATUS_CODE.NOT_IMPLEMENTED
		todos = None
		try:
			target = self.db.session.query(Todo)
			todos = target.filter(filters).all()
			if todos:
				code = STATUS_CODE.OK
			else:
				code = STATUS_CODE.NOT_FOUND 
		except Exception:
			code = STATUS_CODE.INTERNAL_SERVER_ERROR
		return code, todos



