from flask import Blueprint, make_response, request
import json
from functions.user_functions import create_user,authentication
from functions.musician_functions import create_musician, find_one as musicians_findone, find_all as musicians_findall
from functions.orchestre_functions import create_orchestra, orchestra_find_all,orchestra_find_one

routes = Blueprint('routes', __name__)


@routes.route('/user/create', methods=['POST'])
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


@routes.route('/user/SignIn', methods=['POST'])
def sign():
    req = json.loads(request.data.decode('utf8'))
    confirm = authentication( req['user']['password'], req['user']['name'])
    if confirm:
        resp = make_response({
            'SUCCESS': True
        }), 201
    else:
        resp = make_response({
            'ERROR NOT FOUND': False
        }), 404
    return resp


@routes.route('/musician/create', methods=["POST"])
def create_play():
    req = json.loads(request.data.decode('utf8'))
    msc = create_musician(req)
    if msc:
        resp = make_response({
            'SUCCESS': True
        }), 201
    else:
        resp = make_response({
            'ERROR NOT FOUND': False
        }), 404
    return resp


@routes.route('/findOne', methods=["POST"])
def find_first():
    req = json.loads(request.data.decode('utf8'))
    find = musicians_findone(req)
    if find:
        resp = make_response({
            'SUCCESS': True,
            'musician': find
        }), 201
    else:
        resp = make_response({
            'ERROR NOT FOUND': False
        }), 404
    return resp


@routes.route('/findAll', methods=["GET"])
def find_everything():
    finder = musicians_findall()
    if finder:
        resp = make_response({
            'SUCCESS': True,
            'musicians': finder
        }), 201
    else:
        resp = make_response({
            'ERROR NOT FOUND': False
        }), 404
    return resp


@routes.route('/create/orchestra', methods=['POST'])
def create_orche():
    req = json.loads(request.data.decode('utf8'))
    orc = create_orchestra(req)
    if orc:
        resp = make_response({
            'SUCCESS': True,
        }), 201
    else:
        resp = make_response({
            'ERROR NOT FOUND': False
        }), 404
    return resp


@routes.route('/orchestra/findAll', methods=["GET"])
def orchestra_finder():
    finder = orchestra_find_all()
    if finder:
        resp = make_response({
            'SUCCESS': True,
            'musicians': finder
        }), 201
    else:
        resp = make_response({
            'ERROR NOT FOUND': False
        }), 404
    return resp


@routes.route('/orchestra/findOne', methods=['POST'])
def orchestra_findOne():
    req = json.loads(request.data.decode('utf8'))
    find = orchestra_find_one(req)
    if find:
        resp = make_response({
            'SUCCESS': True,
            'orchestra': find
        }), 201
    else:
        resp = make_response({
            'ERROR NOT FOUND': False
        }), 404
    return resp
