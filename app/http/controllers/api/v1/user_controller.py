from flask import request
from flask_restx import Resource, Namespace
from app.http.resources.get_list_user_resouce import format_list_user_response
from storage.doc.request.user_api_document import (
    add_user_request_doc,
    get_list_user_request_doc,
)
from storage.doc.response.user_api_response import (
    add_user_response_doc,
    add_user_response_err_doc,
)
from app.helper.response import response_success, response_error
from app.http.requests.user.add_user_request import validate_add_user
from app.http.requests.user.get_list_user_request import validate_request_get_list_user
from app.services.user_service import add_user, get_list_user

api = Namespace("users", description="Api users")


@api.route("/")
class UserController(Resource):
    # Start api doc create user
    @api.expect(add_user_request_doc(api))
    @api.response(200, "Add user successfully!", model=add_user_response_doc(api))
    @api.response(
        400,
        "Response validate add user input",
        model=add_user_response_err_doc(
            api=api,
            code=400,
            message="Password confirmation need to same password field.",
            errors={
                "password_confirm": "Password confirmation need to same password field."
            },
        ),
    )
    @api.doc("Create a new user")
    # End api doc create user
    @validate_add_user
    def post(seft, valid_data):
        success = add_user(valid_data)
        if success:
            return response_success(data={})
        return response_error(message="Add user failed!")

    # Start api doc get list user
    @api.expect(get_list_user_request_doc())
    @api.response(200, "Get list user successfully!", model=add_user_response_doc(api))
    @api.doc("Get list user successfully!")
    # End api doc get list user
    @validate_request_get_list_user
    def get(seft, valid_data):
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
