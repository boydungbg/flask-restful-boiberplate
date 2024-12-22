from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
import os
import logging
from logging.handlers import RotatingFileHandler

db: SQLAlchemy = SQLAlchemy()


def init_db(app: Flask):
    db.init_app(app)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    Migrate(app, db, directory=f"{BASE_DIR}/migrations")
    return db
