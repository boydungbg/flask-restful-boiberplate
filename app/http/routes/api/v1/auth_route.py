from flask_restx import Resource, Namespace

from app.helper.response import response_error, response_success
from app.http.requests.auth.login_request import validate_login
from app.services.auth_service import login
from storage.doc.request.auth_api_document import login_request_doc
from storage.doc.response.auth_api_response import (
    login_response_doc,
    login_response_err_doc,
)

auth_ns = Namespace("auth", description="Api authorization")


@auth_ns.route("/login")
class LoginRoute(Resource):
    # Start api doc create user
    @auth_ns.expect(login_request_doc(auth_ns))
    @auth_ns.response(200, "Login successfully!", model=login_response_doc(auth_ns))
    @auth_ns.response(
        400,
        "Incorrect email or password.",
        model=login_response_err_doc(
            ns=auth_ns,
            code=400,
            message="Incorrect email or password.",
            errors={},
        ),
    )
    # End api doc create user
    @validate_login
    def post(self, valid_data: dict):
        result = login(
            username=valid_data.get("username"), password=valid_data.get("password")
        )
        if result["status"] == False:
            return response_error(message=result["message"])
        return response_success(data={"access_token": result["data"]})
