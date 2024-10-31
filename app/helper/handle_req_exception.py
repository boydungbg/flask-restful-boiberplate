from flask import Flask
from .response import response_error

def handle_req_exception(app: Flask):
    @app.errorhandler(Exception)
    def handle(error):
        return response_error(code=500)
