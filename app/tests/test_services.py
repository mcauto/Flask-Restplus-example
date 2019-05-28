import pytest
import pysnooper
import mock

from alchemy_mock.mocking import UnifiedAlchemyMagicMock

from app.services.todo_service import get_todos
from app import db
from app.models.todo import Todo

from app.constants import STATUS_CODE

from app.services import __default_response__


def test_default_repsonse(flask_app):
	expect = STATUS_CODE.NOT_IMPLEMENTED
	response = __default_response__()
	assert response.status_code == expect.value


mockTodo = Todo(name="name", done=False)

# db.session mocking
session = UnifiedAlchemyMagicMock(data=[
	(
		[mock.call.query(Todo), 
		 mock.call.filter((Todo.name == mockTodo.name) | (Todo.done == mockTodo.done))
		],
		[mockTodo]
	)
])

class TestTodoService:
	@pysnooper.snoop()
	@mock.patch('app.repository.database.db.session', new=session)
	def test_테스트(self, flask_app):
		# 단위 테스트: 로직 변경에 대한 내부의 케이스가 깨지는 것을 개발 단계에서 탐지
		# 기능 테스트: 특정 기능이 동작 여부 테스트
		# 통합 테스트: 시스템 전체의 정상적인 동작여부 테스트
		response = get_todos(name=mockTodo.name, done=mockTodo.done)
		assert response.status_code == STATUS_CODE.OK.value