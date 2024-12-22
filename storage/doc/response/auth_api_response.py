from flask_restx import Namespace, fields


def login_response_doc(ns: Namespace):
    return ns.model(
        "login_response_doc",
        {
            "code": fields.Integer(200),
            "data": fields.Raw(
                {
                    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ4OTg1NDEsImlhdCI6MTczNDgxMjE0MSwic3ViIjoyfQ.tZT1PUIASnBr7xYyxZVPUf5TNaGmsEaFjxUAtpgGJSA"
                }
            ),
            "message": fields.String("Successfully!"),
        },
    )


def login_response_err_doc(
    ns: Namespace,
    code=400,
    message="Incorrect username or password.",
    errors=[],
):
    return ns.model(
        "login_response_err_doc",
        {
            "code": fields.Integer(code),
            "data": fields.Raw({}),
            "message": fields.String(message),
            "errors": fields.Raw(errors),
        },
    )
