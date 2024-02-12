from app import app
from flask import request, make_response
from .app_config import CorsConfig


@app.route('/status', methods=['GET'])
def index():
    return 'Hello, World!'


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
