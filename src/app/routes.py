from app import app


@app.route('/status', method = ["GET"])
def index():
    return 'OK'