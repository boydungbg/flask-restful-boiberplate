from flask_restx import Namespace, fields

def add_user_request_doc(api: Namespace):
    return api.model(
        "user",
        {
            "email": fields.String(required=True, description="This is your email."),
            "username": fields.String(
                required=True, description="This is your username."
            ),
            "password": fields.String(
                required=True, description="This is your password."
            ),
            "password_confirm": fields.String(
                required=True, description="This is your password confirmation."
            ),
            "full_name": fields.String(
                required=True, description="This is your full name."
            ),
        },
    )
