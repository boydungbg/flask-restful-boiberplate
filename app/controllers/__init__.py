from flask_restx import Api
from flask import Blueprint

from .api.v1.user_controller import api as user_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="Api flask boiberplate",
    version="1.0",
    description="Api flask boiberplate",
    prefix='/api/v1'
)

api.add_namespace(user_ns, path="/users")
