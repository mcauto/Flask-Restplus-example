import pytest
import pysnooper
import mock

from alchemy_mock.mocking import UnifiedAlchemyMagicMock

from app.services.todo_service import get_todos
from app import db
from app.models.todo import Todo

from app.constants import STATUS_CODE

from app.repository.database import TodoRepository
from app.services.todo_service import TodoService

mock_name = "TEST_NAME"
mock_done = False
mock_todo = Todo(name=mock_name, done=mock_done)

FILTERS = {
	'get_todos_by_name_or_done':(
		(Todo.name == mock_todo.name) | (Todo.done == mock_todo.done)
	)
}

QUERIES = {
	'get_todos_by_name_or_done':[
		mock.call.query(Todo), 
		mock.call.filter(FILTERS['get_todos_by_name_or_done'])
	]
}
QUERY_RESULT = {
	'get_todos_by_name_or_done':[mock_todo]
}

# db.session mocking
session = UnifiedAlchemyMagicMock(data=[
	(
		QUERIES['get_todos_by_name_or_done'],
		QUERY_RESULT['get_todos_by_name_or_done']
	)
])

session_path='app.db.session'
class TestTodoRepository:
	@mock.patch(session_path, new=session)
	def test_get_list(self, flask_app):
		# given
		repository = TodoRepository(db=db)
		# when
		filters = FILTERS['get_todos_by_name_or_done']
		code, result = repository.get_list(filters=filters)
		# then
		assert code == STATUS_CODE.OK
		assert result == QUERY_RESULT['get_todos_by_name_or_done']

class TestTodoService:
	@mock.patch(session_path, new=session)
	def test_get_list(self,flask_app):
		# given
		service = TodoService(repository=TodoRepository(db=db))
		# when
		filters = FILTERS['get_todos_by_name_or_done']
		response = service.get_todos(filters=filters)
		assert response.status_code == STATUS_CODE.OK.value
		assert False