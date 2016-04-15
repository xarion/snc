# coding=utf-8

from flask import Flask

from api import bp as api_bp

app = Flask(__name__)

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
