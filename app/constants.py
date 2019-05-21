from enum import Enum

class STATUS_CODE(Enum):
	OK = 200
	CREATED = 201
	NO_CONTENT = 204
	BAD_REQUEST = 400
	UNAUTHORIZED = 401
	FORBIDDEN = 403
	NOT_FOUND = 404
	METHOD_NOT_ALLOWED = 405
	CONFLICT = 409	
	INTERNAL_SERVER_ERROR = 500
	NOT_IMPLEMENTED = 501
	BAD_GATEWAY = 502

responses = {item.value: item.name for item in STATUS_CODE}

def support_codes(unsupport_codes):
	unsupport_codes = [code.value for code in unsupport_codes]
	return {code: name for code, name in responses.items() if code not in unsupport_codes}
	
GET = support_codes(unsupport_codes=[
						STATUS_CODE.CREATED, STATUS_CODE.NO_CONTENT,
						STATUS_CODE.CONFLICT,
						STATUS_CODE.METHOD_NOT_ALLOWED,
						STATUS_CODE.NOT_IMPLEMENTED])
POST = support_codes(unsupport_codes=[
						STATUS_CODE.OK, STATUS_CODE.NO_CONTENT,
						STATUS_CODE.METHOD_NOT_ALLOWED,
						STATUS_CODE.NOT_IMPLEMENTED])
PATCH = support_codes(unsupport_codes=[
						STATUS_CODE.CREATED,
						STATUS_CODE.NO_CONTENT,
						STATUS_CODE.METHOD_NOT_ALLOWED,
						STATUS_CODE.NOT_IMPLEMENTED])
DELETE = support_codes(unsupport_codes=[
						STATUS_CODE.CREATED,
						STATUS_CODE.CONFLICT,
						STATUS_CODE.METHOD_NOT_ALLOWED,
						STATUS_CODE.NOT_IMPLEMENTED])
