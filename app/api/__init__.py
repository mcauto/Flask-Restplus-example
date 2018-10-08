from flask import Flask, Blueprint
from flask_restful import Api

from app.books.views import BookItem

api_blueprint = Blueprint('books', "Book's API")
api = Api(api_blueprint)
api.add_resource(BookItem, '/books/<int:book_id>')

