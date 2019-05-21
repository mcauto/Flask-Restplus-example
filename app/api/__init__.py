from flask import Blueprint
from flask_restplus import Api

from .resources.todo import api as todo_api

# https://flask-restplus.readthedocs.io/en/stable/swagger.html#documenting-authorizations
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}
blueprint = Blueprint('api', __name__, 
						  url_prefix='/api')
rest_api = Api(blueprint, 
                doc='/doc',
                security=['apikey'], 
                authorizations=authorizations,
                title='Flask RESTPlus API',
                version='1.0',
                description='flask RESTPlus API')

rest_api.add_namespace(todo_api, '/todo')
