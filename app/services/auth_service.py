from typing import Union
import jwt
import datetime
from app.models.user import User
from config.app import AppConfig
from extensions.bcrypt import flask_bcrypt


def login(username: str, password: str) -> str:
    data: User = User.query.where(User.username == username).first()
    if data == None:
        return {"status": False, "message": "Incorrect username or password!"}
    if _check_password(password_hash=data.password_hash, password=password) == False:
        return {"status": False, "message": "Incorrect username or password!"}
    token = _encode_auth_token(data.id)
    return {"status": True, "data": token}


def _check_password(password_hash, password: str) -> bool:
    return flask_bcrypt.check_password_hash(password_hash, password)


def _encode_auth_token(user_id: int) -> bytes:
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "sub": user_id,
        }
        return jwt.encode(payload, AppConfig.app_secret_key, algorithm="HS256")
    except Exception as e:
        return e


def decode_auth_token(auth_token: str) -> Union[str, int]:
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        if auth_token.startswith("Bearer "):
            auth_token = auth_token[7:]
        payload = jwt.decode(auth_token, AppConfig.app_secret_key, algorithms="HS256")
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return "Signature expired. Please log in again."
    except jwt.InvalidTokenError:
        return "Invalid token. Please log in again."
