import re
from marshmallow import Schema, fields, ValidationError
from flask import request
from app.helper.response import response_error


class _LoginSchemaRequest(Schema):
    username = fields.String(
        required=True,
        error_messages={
            "required": "Username is required.",
        },
    )
    password = fields.String(
        required=True,
        error_messages={
            "required": "Password is required.",
        },
    )


def validate_login(func):
    login_schema = _LoginSchemaRequest()

    def decorate(*args, **kwargs):
        try:
            valid_data = login_schema.load(request.get_json())
            kwargs["valid_data"] = valid_data  # Pass to the view function
            return func(*args, **kwargs)
        except ValidationError as err:
            first_messages = {
                field: messages[0] for field, messages in err.messages.items()
            }
            return response_error(
                errors=first_messages,
                code=400,
                message=next(iter(first_messages.values()), "Add user faild."),
            )

    return decorate
