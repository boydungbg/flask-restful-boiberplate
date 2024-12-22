from flask import Flask
from werkzeug.exceptions import NotFound
from app.exception.auth_exception import AuthException
from config.app import AppConfig
from .response import response_error


def handle_req_exception(app: Flask):
    @app.errorhandler(Exception)
    def handle(error):
        if isinstance(error, NotFound):
            return response_error(code=404, message="Not found!", errors=[])
        elif isinstance(error, AuthException):
            return response_error(code=401, message="Unauthorized!", errors=[])
        app.logger.error(error, stack_info=True)
        return response_error(code=500)
