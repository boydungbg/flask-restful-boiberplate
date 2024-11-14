import re
from marshmallow import Schema, fields, ValidationError, post_load, validates
from flask import request
from app.helper.response import response_error
from app.services.user_service import is_email_exist, is_username_exist


class _AddUserSchemaRequest(Schema):
    username = fields.String(
        required=True,
        error_messages={
            "required": "Username is required.",
        },
    )
    email = fields.Email(
        required=True,
        error_messages={
            "required": "Email is required.",
            "invalid": "Email address is not valid.",
        },
    )
    password = fields.String(
        required=True,
        error_messages={
            "required": "Password is required.",
        },
    )
    password_confirm = fields.String(
        required=True,
        error_messages={
            "required": "Password confirm is required.",
        },
    )
    full_name = fields.String(
        required=True,
        error_messages={
            "required": "Full name is required.",
        },
    )

    @validates("full_name")
    def validate_full_name(self, full_name: str):
        # pattern = r"^[A-Za-zÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹỶỸỴÝỪỬŨÙú\s ]+(?: [A-Za-zÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠƯạảấầẫậẵệẹẻẽềẽễễẽẽễẹệịụủứừửựôơơữựỷỸửỳỹ\s]+)*$"
        if not (10 <= len(full_name.strip()) <= 32):
            raise ValidationError("Full name must be between 6 and 32 characters long.")
        # if not re.match(pattern, full_name.strip()):
        #     raise ValidationError(
        #         "Full name must start with a letter or underscore and can only contain letters, digits, and underscores."
        #     )

    @validates("username")
    def validate_username(self, username):
        if not (6 <= len(username) <= 32):
            raise ValidationError("Username must be between 6 and 32 characters long.")
        if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", username):
            raise ValidationError(
                "Username must start with a letter or underscore and can only contain letters, digits, and underscores."
            )

    @validates("password")
    def validate_password(self, password):
        password_regex = re.compile(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        )
        if not password_regex.match(password):
            raise ValidationError(
                "Password must be at least 8 characters long, "
                "contain at least one uppercase letter, "
                "one lowercase letter, one digit, and one special character."
            )

    @post_load
    def check_passwords(self, data: dict, **kwargs):
        if data["password"] != data["password_confirm"]:
            raise ValidationError(
                "Passwords and Password confirm do not match.", "password_confirm"
            )
        if is_email_exist(data.get("email")):
            raise ValidationError("Email has been used", "email")
        if is_username_exist(data.get("username")):
            raise ValidationError("Username has been used", "username")
        return data


def validate_add_user(func):
    add_user_schema = _AddUserSchemaRequest()

    def decorate(*args, **kwargs):
        try:
            valid_data = add_user_schema.load(request.get_json())
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
