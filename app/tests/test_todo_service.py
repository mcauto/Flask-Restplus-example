import pytest
import pysnooper
import mock

from alchemy_mock.mocking import UnifiedAlchemyMagicMock

from app.services.todo_service import get_todos
from app import db
from app.models.todo import Todo

from app.constants import STATUS_CODE

mockTodo = Todo(name="name", done=False)

# db.session mocking
session = UnifiedAlchemyMagicMock(data=[
	(
		[mock.call.query(Todo), 
		mock.call.filter(Todo.name == mockTodo.name, Todo.done == mockTodo.done)
		],
		[mockTodo]
	)
])

class TestTodoService:
	@pysnooper.snoop()
	@mock.patch('app.repository.database.db.session', new=session)
	def test_테스트(self, flask_app):
		response = get_todos(name=mockTodo.name, done=mockTodo.done)
		assert response.status_code == STATUS_CODE.OK.value