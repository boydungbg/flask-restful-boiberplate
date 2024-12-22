from flask import Flask
from config.database import DatabaseConfig
from config.log import config_log
from database import init_db
from config.api import blueprint
from app.helper.handle_req_exception import handle_req_exception


def create_app():
    app = Flask(__name__)
    DatabaseConfig.config_database(app)
    handle_req_exception(app)
    init_db(app)
    config_log(app)
    app.register_blueprint(blueprint)
    return app
