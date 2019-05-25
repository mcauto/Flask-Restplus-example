from flask import make_response
from flask import Response
from flask import jsonify

from app.constants import STATUS_CODE

def __default_response__():
	result = STATUS_CODE.NOT_IMPLEMENTED
	body = jsonify({"message":result.name})
	status_code = result.value
	return body, status_code