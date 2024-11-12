from flask import Flask

from config.app import AppConfig
from .response import response_error

def handle_req_exception(app: Flask):
    @app.errorhandler(Exception)
    def handle(error):
        if (AppConfig.app_development == "true"):
            print(error)
        return response_error(code=500)
