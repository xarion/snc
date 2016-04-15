# coding=utf-8

from flask import Flask

from api import bp as api_bp
from sockets import socket

app = Flask(__name__)

app.register_blueprint(api_bp)
socket.init_app(app)

if __name__ == '__main__':
    app.debug = True
    socket.io.run(app, host="0.0.0.0")
