import jwt
import datetime
from typing import Union
from database import db
from extensions.bcrypt import flask_bcrypt
from config.app import AppConfig 


class User(db.Model):
    __tablename__ = "users"  # Table name in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    username = db.Column(db.String(100), nullable=False)  # Name column
    full_name = db.Column(db.String(255), nullable=False)  # Name column
    email = db.Column(db.String(100), unique=True, nullable=False)  # Email column
    password_hash = db.Column(db.String(255), nullable=False)  # Password column

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def encode_auth_token(user_id: int) -> bytes:
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(days=1, seconds=5),
                "iat": datetime.datetime.utcnow(),
                "sub": user_id,
            }
            return jwt.encode(payload, AppConfig.app_secret_key, algorithm="HS256")
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token: str) -> Union[str, int]:
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, AppConfig.app_secret_key)
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
