from app import app
from flask import request, make_response
from typing import List
from werkzeug.exceptions import BadRequest
from .app_config import CorsConfig
from .dto import card_list_schema, CardList
from .test import RandomCardList

import json


@app.route('/status', methods=['GET'])
def index():
    return 'Ok'


@app.route('/data_test', methods=['POST'])
def get_post() -> List[CardList]:
    # Delete this route after testing
    try:
        dto_data = card_list_schema.load(request.get_json())
        return dto_data # type: ignore
    except json.JSONDecodeError:
        raise BadRequest('Invalid data')


@app.route('/data_test', methods=['GET'])
def get_test() -> List[CardList]:
    # Delete this route after testing
    card_list = RandomCardList().get_card_list()
    return card_list_schema.dump(card_list)


@app.after_request
def after_request_func(response):
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization,'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, OPTIONS, PUT, PATCH, DELETE'
        )
        if origin in CorsConfig.ORIGINS:
            response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin in CorsConfig.ORIGINS:
            response.headers.add('Access-Control-Allow-Origin', origin)

    return response
