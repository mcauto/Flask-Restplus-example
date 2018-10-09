from app.books.views import books_api
from app.books.views import BookItem
from app.books.views import BooksList
from flask_restful import Api

api = Api(books_api)
api.add_resource(BookItem, '/<int:book_id>')
api.add_resource(BooksList, '/')
