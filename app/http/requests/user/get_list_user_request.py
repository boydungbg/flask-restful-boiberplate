import re
from marshmallow import Schema, fields, ValidationError, validate, validates_schema
from flask import request
from app.helper.response import response_error
from datetime import datetime


class GetListUserRequest(Schema):
    search = fields.String(
        error_messages={
            "invalid": "Search must be a string",
        },
        default="",
        required=False,
    )
    page = fields.Integer(
        error_messages={
            "invalid": "Page must be a number",
        },
        default=1,
    )
    per_page = fields.Integer(
        error_messages={
            "invalid": "Per_page must be a number",
        },
        default=20,
    )
    sort_by = fields.String(
        validate=validate.OneOf(["id", "full_name", "username", "email", 'created_at']),
        description="User sort by: can be 'id', 'full_name', 'username', 'email', 'created_at'",
        required=False,
        default='created_at'
    )
    sort_type = fields.String(
        validate=validate.OneOf(["asc", "desc"]),
        description="User sort type asc or desc",
        required=False,
        default='desc'
    )
    created_at_min = fields.DateTime(
        format="%Y-%m-%d %H:%M:%S",
        error_messages={"invalid": "Invalid date format. Use YYYY-MM-DD HH:MM:SS"},
        required=False,
    )
    created_at_max = fields.DateTime(
        format="%Y-%m-%d %H:%M:%S",
        error_messages={"invalid": "Invalid date format. Use YYYY-MM-DD HH:MM:SS"},
        required=False,
    )

    @validates_schema
    def validate_date_order(self, data: dict, **kwargs):
        start_date: datetime = data.get("created_at_min")
        end_date: datetime = data.get("created_at_max")
        if start_date and end_date and start_date > end_date:
            raise ValidationError(
                "created_at_min must be before created_at_max.", "created_at_min"
            )


def validate_request_get_list_user(func):
    schema = GetListUserRequest()

    def decorate(*args, **kwargs):
        try:
            # Load and validate data
            valid_data = schema.dump(request.args)
            kwargs['valid_data'] = valid_data  # Pass to the view function
            return func(*args, **kwargs)
        except ValidationError as err:
            first_messages = {
                field: messages[0] for field, messages in err.messages.items()
            }
            return response_error(
                errors=first_messages,
                code=400,
                message=next(iter(first_messages.values()), "Failed!"),
            )

    return decorate
