from flask import jsonify
from flask import make_response
from flask import Blueprint

from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse
from flask_restful import abort
from flask_restful import fields
from flask_restful import marshal_with

from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from app.books.models import Books
from app.books.models import BooksSchema
from app.api.database import db

books_api = Blueprint('books', "Book's API")
schema = BooksSchema()
book_fields = {
    'id': fields.Integer,
	'name': fields.String,
    'is_rent': fields.Boolean
}
class BookItem(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('name', type=str, help="book's name",location='json')
	parser.add_argument('is_rent', type=int, help='is it rentable?',location='json')
	body = ''
	status_code = 501 # NOT_IMPLEMENTED
	def get(self, book_id):
		book_query = Books.query.get_or_404(book_id)
		book = schema.dump(book_query).data
		return book

	def patch(self, book_id):
		args = self.parser.parse_args()
		book = Books.query.get_or_404(book_id)
		for key, value in args.items():
			setattr(book, key, value)
		try:
			book.update()
			self.body = jsonify(schema.dump(book).data)
			self.status_code = 200 # OK
		except IntegrityError as error:
			db.session.rollback()
			error_message = str(error) 
			self.body = jsonify({"error": error_message, "type":"IntegrityError"})
			if "Duplicate entry" in error_message:
				self.status_code = 409 # CONFLICT
			else:
				self.status_code = 400 # BAD REQUEST
		finally:
			response = (self.body, self.status_code.value)
			response = make_response(response)

		return response

	def delete(self, book_id):
		return {'book_id': book_id, 'method':'delete'}

class BooksList(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('name', required=True, type=str, help="book's name",location='json')
	parser.add_argument('is_rent', type=int, help='is it rentable?',location='json')
	body = ''
	status_code = 501

	def get(self):
		books_query = Books.query.all()
		results = schema.dump(books_query, many=True).data
		self.body = jsonify(results)
		self.status_code = 200
		response = (self.body, self.status_code)
		return make_response(response)

	def post(self):
		args = self.parser.parse_args()
		book = Books(name=args['name'],
					is_rent=args['is_rent'])
		try:
			book.add(book) 
			query = Books.query.get(book.id)
			self.body = jsonify(schema.dump(query).data)
			self.status_code = 201

		except IntegrityError as error:
			db.session.rollback()
			import os
			error_message = str(error) 
			self.body = jsonify({"error": str(error), "type":"IntegrityError"})
			if "Duplicate entry" in error_message:
				self.status_code = 409
			else:
				self.status_code = 400
		finally:
			response = (self.body, self.status_code.value)
			response = make_response(response)

		return response
