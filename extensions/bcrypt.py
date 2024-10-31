from flask_bcrypt import Bcrypt
from flask import Flask

flask_bcrypt:Bcrypt = None

def init_bcrypt(app: Flask):
    flask_bcrypt = Bcrypt(app)
    return flask_bcrypt
