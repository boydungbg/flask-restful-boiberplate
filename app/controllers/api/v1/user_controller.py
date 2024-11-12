from flask import request
from flask_restx import Resource, Namespace
from app.doc.request.user import add_user_request_doc
from app.doc.response.user import add_user_response_doc, add_user_response_err_doc
from app.helper.response import response_success
from app.requests.add_user_request import validate_add_users

api = Namespace("users", description="Api users")

@api.route("/")
class UserController(Resource):
    # Start create api doc
    @api.expect(add_user_request_doc(api))
    @api.response(200, "Add user successfully!", model=add_user_response_doc(api))
    @api.response(
        400,
        "Response validate add user input",
        model=add_user_response_err_doc(
            api=api, code=400, message="Password confirmation need to same password field.", errors={"password_confirm": "Password confirmation need to same password field."}
        ),
    )
    @api.doc("Create a new user")
    # End create api doc
    @validate_add_users
    def post(seft):
        data = request.valid_data
        return response_success(data=data)
