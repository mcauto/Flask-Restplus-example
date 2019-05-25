from typing import List
from typing import Dict

from flask import Response
from flask import make_response
from flask import jsonify


from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from app.repository.database import db
from app.models.todo import Todo, TodoSchema
from app.services import __default_response__

from app.constants import STATUS_CODE

"""
TODO: Service Class Refactoring
"""

def get_todos(name: str, done: bool)-> Response:
	body, status = __default_response__()
	target = db.session.query(Todo)

	if name and done:
		query = target.filter((Todo.name == name) | (Todo.done == done))
	elif name:
		query = target.filter((Todo.name)== name)
	elif done:
		query = target.filter((Todo.done) == done)
	else:
		query = target

	todos = query.all()
	if len(todos)>0:
		todos = TodoSchema().dump(todos, many=True).data
		body = jsonify(todos)
		status_code = STATUS_CODE.OK.value
	else:
		body = jsonify({"message":STATUS_CODE.NOT_FOUND.name})
		status_code = STATUS_CODE.NOT_FOUND.value	
	response = make_response(body, status_code)
	return response

def store_todos(todo: Todo)-> Response:
	body, status = __default_response__()
	try:
		# WARNING: https://docs.sqlalchemy.org/en/13/orm/persistence_techniques.html#bulk-operations
		# db.session.bulk_save_objects(todos)
		db.session.add(todo)
		db.session.commit()
		body = jsonify(TodoSchema().dump(todo).data)
		status_code = STATUS_CODE.CREATED.value
	except IntegrityError as err:
		db.session.rollback()
		error_message = str(error) 
		body = jsonify({"error": error_message})
		if "Duplicate entry" in error_message:
			status_code = STATUS_CODE.CONFLICT.value
		else:
			status_code = STATUS_CODE.BAD_REQUEST.value

	return make_response(body, status_code)

def patch_todos(todo: Todo, args: Dict) -> Response:
	body, status = __default_response__()
	try:
		for key, value in args.items():
			setattr(todo, key, value)
		db.session.commit()
		body = jsonify(TodoSchema().dump(todo).data)
		status_code = STATUS_CODE.OK.value
	except IntegrityError as error:
		db.session.rollback()
		error_message = str(error) 
		body = jsonify({"error": error_message})
		if "Duplicate entry" in error_message:
			status_code = STATUS_CODE.CONFLICT.value
		else:
			status_code = STATUS_CODE.BAD_REQUEST.value

	return make_response(body, status_code)

def delete_todos(todo: Todo)-> Response:
	body, status_code = __default_response__()
	db.session.delete(todo)
	db.session.commit()
	body = jsonify({"message":"success"})
	status_code = STATUS_CODE.NO_CONTENT.value
	return make_response(body, status_code)