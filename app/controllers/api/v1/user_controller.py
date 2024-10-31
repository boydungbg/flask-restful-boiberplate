from flask import request
from flask_restx import Resource, Namespace
from app.doc.request.user import add_user_request_doc
from app.doc.response.user import add_user_response_doc, add_user_response_err_doc
from app.helper.response import response_success

api = Namespace("users", description="Api users")

@api.route("/")
class UserController(Resource):
    # Start create api doc
    @api.expect(add_user_request_doc(api))
    @api.response(200, "Add user successfully!", model=add_user_response_doc(api))
    @api.response(
        500,
        "Add user failed!",
        model=add_user_response_err_doc(
            api=api, code=400, message="Add user failed!", errors=["Add user failed!"]
        ),
    )
    @api.doc("Create a new user")
    # End create api doc
    def post(seft):
        data = {"Hello": "wourl"}
        return response_success(data=data)
