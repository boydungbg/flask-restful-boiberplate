from marshmallow import Schema, fields, ValidationError, post_load, validates
from flask import request
from app.helper.response import response_error
import re

class _AddUserSchemaRequest(Schema):
  username = fields.String(required=True, error_messages={
    'required':'Username is required.',
  })
  email = fields.Email(required=True, error_messages={
    'required':'Email is required.',
    'invalid': 'Email address is not valid.'
  })
  password = fields.String(required=True, error_messages={
    'required':'Password is required.',
  })
  confirm_password = fields.String(required=True,  error_messages={
    'required':'Password confirm is required.',
  })
  full_name = fields.String(required=True,  error_messages={
    'required':'Full name is required.',
  })
  
  @validates('username')
  def validate_username(self, username):
    if not (6 <= len(username) <= 32):
        raise ValidationError("Username must be between 6 and 32 characters long.")
    if not re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', username):
        raise ValidationError("Username must start with a letter or underscore and can only contain letters, digits, and underscores.")
  
  @validates('password')
  def validate_password(self, password):
    password_regex = re.compile(
      r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    )
    if not password_regex.match(password):
        raise ValidationError(
            "Password must be at least 8 characters long, "
            "contain at least one uppercase letter, "
            "one lowercase letter, one digit, and one special character."
        )

  @post_load
  def check_passwords(self, data, **kwargs):
      if data['password'] != data['confirm_password']:
          raise ValidationError("Passwords and Password confirm do not match.", "confirm_password")
      return data

def validate_add_users(func):
  add_user_schema = _AddUserSchemaRequest()
  def decorate(*args, **kwargs):
    try:
      request.valid_data = add_user_schema.load(request.json)
      return func(*args, **kwargs)
    except ValidationError as err:
      first_messages = {field: messages[0] for field, messages in err.messages.items()}
      return response_error(errors= first_messages, code=400, message=next(iter(first_messages.values()), 'Add user faild.'))
  return decorate
    