from marshmallow import Schema, fields, ValidationError

class AddUserSchemaRequest(Schema):
  email = fields.Email(required=True,)
  password = fields.String(required=True)
  password_comfirmation = fields.String(required=True)
  full_name = fields.String(required=True)
  username = fields.String(required=True)

