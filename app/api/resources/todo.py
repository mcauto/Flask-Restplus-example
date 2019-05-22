from flask import Blueprint
from flask import jsonify
from flask import make_response
from flask import request

from flask_restplus import Api
from flask_restplus import Resource
from flask_restplus import Namespace
from flask_restplus import fields
from flask_restplus import reqparse
from flask_restplus import inputs
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError

from app.constants import STATUS_CODE
from app.constants import GET,POST,PATCH,DELETE

from app.repository.database import db
from app.models.todo import Todo, TodoSchema
from app.services.todo_service import get_todos


api = Namespace('Todo',description="Todo's REST API")
schema = TodoSchema()
todo_fields = api.model('Todo', {
	'name': fields.String(required=True, description="Todo's name"),
	'done': fields.Boolean(description="Todo's status"),
})

@api.route('/<int:todo_id>')
@api.param('todo_id', 'Todo identifier')
class TodoItem(Resource):
	parser = reqparse.RequestParser(bundle_errors=True)
	parser.add_argument('name', type=str, help="todo's name",location='args')
	parser.add_argument('done', type=bool, help="todo's status",location='args')

	post_parser = reqparse.RequestParser(bundle_errors=True)
	post_parser.add_argument('name', required=True, type=str, help="todo's name",location='json')
	post_parser.add_argument('done', type=str, help="todo's status",location='json')

	@api.doc(responses=GET, security='apikey', parser=parser)
	def get(self, todo_id):
		pass
	
	@api.expect(todo_fields)
	@api.doc(responses=PATCH, security='apikey', parser=post_parser)
	def patch(self, todo_id):
		pass

	@api.doc(responses=DELETE, security='apikey')
	def delete(self, todo_id):
		pass
		
@api.route('s')
class TodoList(Resource):
	parser = reqparse.RequestParser(bundle_errors=True)
	parser.add_argument('name', type=str, help="todo's name",location='args')
	parser.add_argument('done', type=inputs.boolean, help="todo's status",location='args')

	post_parser = reqparse.RequestParser(bundle_errors=True)
	post_parser.add_argument('name', required=True, type=str, help="todo's name",location='json')

	@api.doc(responses=GET, security='apikey', parser=parser)
	def get(self):
		args = self.parser.parse_args()
		print(request.json)
		print(args)
		return get_todos(args['name'], args['done'])

	@api.expect(todo_fields)
	@api.doc(responses=POST, security='apikey', parser=post_parser)
	def post(self):
		args = self.post_parser.parse_args()
		pass
