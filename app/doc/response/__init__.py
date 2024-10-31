from flask_restx import Namespace, fields


def response_success_doc(func):
    def decorating(*args, **kwargs):
        return args[0].model(
            "Reponse success",
            {
                "code": fields.Integer(200),
                "data": fields.Raw(func(*args, **kwargs)),
                "message": fields.String("Successfully!"),
            },
        )

    return decorating


def response_error_doc(func):
    def decorating(*args, **kwargs):
        return kwargs["api"].model(
            "Reponse error",
            {
                "code": fields.Integer(kwargs["code"]),
                "data": fields.Raw({}),
                "message": fields.String(kwargs["message"]),
                "errors": fields.Raw(func(*args, **kwargs)),
            },
        )

    return decorating
