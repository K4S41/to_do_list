from app import app


@app.route('/status', methods=['GET'])
def index():
    return 'OK'
