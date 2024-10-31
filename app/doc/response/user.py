from flask_restx import Namespace
from . import response_error_doc, response_success_doc


@response_success_doc
def add_user_response_doc(api: Namespace):
    return {}


@response_error_doc
def add_user_response_err_doc(
    api: Namespace,
    code=400,
    message="Something wrong!",
    errors=[],
):
    return {}
