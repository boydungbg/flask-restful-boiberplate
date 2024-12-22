from flask_restx import Namespace, fields, reqparse


def login_request_doc(ns: Namespace):
    return ns.model(
        "login_request_doc",
        {
            "username": fields.String(
                required=True,
                description="This is your username.",
                default="username",
            ),
            "password": fields.String(
                required=True, description="This is your password.", default="Password"
            ),
        },
    )
