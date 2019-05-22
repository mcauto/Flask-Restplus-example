from typing import List

from flask import Response
from flask import make_response
from flask import jsonify

from app.repository.database import db
from app.models.todo import Todo, TodoSchema

from app.constants import STATUS_CODE


def get_todos(name: str, done: bool)-> Response:
	print(name, done)
	todos = db.session.query(Todo).filter(Todo.name == name, Todo.done == done).all()
	if len(todos)>0:
		todos = TodoSchema().dump(todos, many=True).data
		body = jsonify(todos)
		status_code = STATUS_CODE.OK.value
	else:
		body = jsonify({"message":STATUS_CODE.NOT_FOUND.name})
		status_code = STATUS_CODE.NOT_FOUND.value	
	response = make_response(body, status_code)
	return response


