from app.config import get_con
from flask import Blueprint, make_response, request
import json
from functions.user_functions import create_user

routes = Blueprint('routes',__name__)

@routes.route('/user/create', methods = ['POST'])
def create():
    req = json.loads(request.data.decode('utf8'))
    usr = create_user(req)
    if usr:
        resp = make_response(
            {
                'Success': True
            }
        ),200

    else:
        resp = make_response({
            'message': 'Not Found'
        }),404

    return resp
