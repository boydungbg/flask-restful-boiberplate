from flask import jsonify


def response_success(data=[], message="Successfully"):
    return jsonify({"code": 200, "data": data, "message": message})


def response_error(errors=["Something wrong!"], code=400, message="Something wrong!"):
    return jsonify({"code": code, "data": {}, "message": message, "errors": errors})
