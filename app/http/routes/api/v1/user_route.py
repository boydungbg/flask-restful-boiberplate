from flask_restx import Resource, Namespace

from app.http.middleware.auth_middleware import auth
from app.http.resources.user.get_list_user_resouce import format_list_user_response
from storage.doc.request.user_api_document import (
    add_user_request_doc,
    get_list_user_request_doc,
)
from storage.doc.response.user_api_response import (
    add_user_response_doc,
    add_user_response_err_doc,
    get_list_user_response_doc,
)
from app.helper.response import response_success, response_error
from app.http.requests.user.add_user_request import validate_add_user
from app.http.requests.user.get_list_user_request import validate_request_get_list_user
from app.services.user_service import add_user, get_list_user

user_ns = Namespace(
    "users",
    description="Api users",
)


@user_ns.route("/")
class UserRoute(Resource):
    # Start api doc create user
    @user_ns.expect(add_user_request_doc(user_ns))
    @user_ns.response(200, "Add user successfully!", add_user_response_doc(user_ns))
    @user_ns.response(
        400,
        "Response validate add user input",
        add_user_response_err_doc(
            ns=user_ns,
            code=400,
            message="Password confirmation need to same password field.",
            errors={
                "password_confirm": "Password confirmation need to same password field."
            },
        ),
    )
    # End api doc create user
    @auth
    @validate_add_user
    def post(self, valid_data):
        success = add_user(valid_data)
        if success:
            return response_success(data={})
        return response_error(message="Add user failed!")

    # Start api doc get list user
    @user_ns.expect(get_list_user_request_doc())
    @user_ns.response(
        200, "Get list user successfully!", model=get_list_user_response_doc(user_ns)
    )
    # End api doc get list user
    @auth
    @validate_request_get_list_user
    def get(self, valid_data):
        result = get_list_user(valid_data)
        if result["status"] == True:
            return response_success(
                data={
                    "items": format_list_user_response(result["data"]),
                    "meta_data": result.get("meta_data"),
                }
            )
        else:
            return response_error(message="Can not get list user!")
