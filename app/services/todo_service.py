from typing import List

from flask import Response
from flask import make_response
from flask import jsonify


from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from app.repository.database import db
from app.models.todo import Todo, TodoSchema

from app.constants import STATUS_CODE

def get_all_todos()-> Response:
	todos = db.session.query(Todo).all()
	if len(todos)>0:
		todos = TodoSchema().dumps(todos, many=True).data
		body = jsonify(todos)
		status_code = STATUS_CODE.OK.value
	else:
		body = jsonify({'message':STATUS_CODE.NOT_FOUND.name})
		status_code = STATUS_CODE.NOT_FOUND.value
	response = make_response(body, status_code)
	return response

def get_todos(name: str, done: bool)-> Response:
	todos = db.session.query(Todo).filter(or_(Todo.name == name, Todo.done == done)).all()
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
	try:
		# WARNING: https://docs.sqlalchemy.org/en/13/orm/persistence_techniques.html#bulk-operations
		# db.session.bulk_save_objects(todos)
		db.session.add(todo)
		db.session.commit()
		query = resource.query.get(resource.id)
		body = jsonify(schema.dump(resource).data)
		status_code = STATUS_CODE.CREATED.value
	except IntegrityError as err:
		db.session.rollback()
		body = jsonify({'message':str(err)})
		status_code = STATUS_CODE.CONFLICT.value
		print(str(err))

	return make_response(body, status_code)


