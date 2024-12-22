from app.exception.auth_exception import AuthException
from flask import request

from app.services.auth_service import decode_auth_token
from app.services.user_service import get_user_by_id


def auth(func):
    def decorate(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token == None:
            raise AuthException()
        user_id = decode_auth_token(auth_token=token)
        if user_id == None:
            raise AuthException()
        user = get_user_by_id(user_id)
        if user == None:
            raise AuthException()
        request.user = user
        return func(*args, **kwargs)
    return decorate
