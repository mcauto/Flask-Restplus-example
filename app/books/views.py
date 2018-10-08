from flask_restful import Resource

class BookItem(Resource):
	def get(self, book_id):
		return {'book_id': book_id, 'method': 'get'}

	def patch(self, book_id):
		return {'book_id': book_id, 'method':'patch'}

	def delete(self, book_id):
		return {'book_id': book_id, 'method':'delete'}



	
	
