from flask_restx import Namespace, fields, reqparse

def add_user_request_doc(ns: Namespace):
    return ns.model(
        "add_user_request_doc",
        {
            "email": fields.String(
                required=True,
                description="This is your email.",
                default="test.email@gamil.com",
            ),
            "username": fields.String(
                required=True, description="This is your username.", default="testuser"
            ),
            "password": fields.String(
                required=True, description="This is your password.", default="Test@1234"
            ),
            "password_confirm": fields.String(
                required=True,
                description="This is your password confirmation.",
                default="Test@1234",
            ),
            "full_name": fields.String(
                required=True,
                description="This is your full name.",
                default="Kimily John",
            ),
        },
    )


def get_list_user_request_doc():
    user_parser = reqparse.RequestParser()
    user_parser.add_argument(
        "search",
        type=str,
        required=False,
        help="Filter by id, username, full_name, email",
    )
    user_parser.add_argument("page", type=int, required=False, help="Page")
    user_parser.add_argument(
        "per_page", type=int, required=False, help="Per item in page"
    )
    user_parser.add_argument(
        "status",
        type=int,
        required=False,
        help="filter with status",
        choices=["0", "1"],
    )
    user_parser.add_argument(
        "sort_by",
        type=str,
        required=False,
        help="Sort by id, username, full_name, email",
        choices=["id", "full_name", "email", "username", "created_at"],
    )
    user_parser.add_argument(
        "sort_type",
        type=str,
        required=False,
        help="Sort type asc or desc",
        choices=["asc", "desc"],
    )
    user_parser.add_argument(
        "created_at_min",
        type=str,
        required=False,
        help="Filter from start date to end date create user. Use format YYYY-MM-DD HH:MM:SS",
    )
    user_parser.add_argument(
        "created_at_max",
        type=str,
        required=False,
        help="Filter from start date to end date create user. Use format YYYY-MM-DD HH:MM:SS",
    )
    return user_parser
