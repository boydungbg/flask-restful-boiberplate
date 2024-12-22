from flask_restx import Api
from flask import Blueprint

from app.http.routes.api.v1.user_route import user_ns
from app.http.routes.api.v1.auth_route import auth_ns

blueprint = Blueprint("api", __name__, url_prefix="/api")
authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}
api = Api(
    blueprint,
    title="Api flask boiberplate",
    version="1.0",
    description="Api flask boiberplate",
    prefix="/v1",
    security=["apikey"],
    authorizations=authorizations,
)

api.add_namespace(
    auth_ns,
    path="/auth",
)
api.add_namespace(ns=user_ns, path="/users")
