from flask_restx import Namespace, fields


def add_user_response_doc(ns: Namespace):
    return ns.model(
        "add_user_response_doc",
        {
            "code": fields.Integer(200),
            "data": fields.Raw({}),
            "message": fields.String("Successfully!"),
        },
    )


def get_list_user_response_doc(
    ns: Namespace,
):
    return ns.model(
        "get_list_user_response_doc",
        {
            "code": fields.Integer(200),
            "data": fields.Raw(
                {
                    "items": [
                        {
                            "created_at": "2024-12-19T15:59:44",
                            "email": "dungle.dev2412@gmail.com",
                            "full_name": "Le Chi Dung",
                            "id": 1,
                            "last_login": None,
                            "username": "dungledev3",
                        },
                        {
                            "created_at": "2024-12-19T16:07:21",
                            "email": "dungle.dev24@gmail.com",
                            "full_name": "Le Chi Dung",
                            "id": 2,
                            "last_login": None,
                            "username": "dungledev",
                        },
                    ],
                    "meta_data": {
                        "count": 2,
                        "current_page": 1,
                        "per_page": 3,
                        "total_page": 1,
                    },
                }
            ),
            "message": fields.String("Successfully!"),
        },
    )


def add_user_response_err_doc(
    ns: Namespace,
    code=400,
    message="Something wrong!",
    errors=[],
):
    return ns.model(
        "add_user_response_err_doc",
        {
            "code": fields.Integer(code),
            "data": fields.Raw({}),
            "message": fields.String(message),
            "errors": fields.Raw(errors),
        },
    )
