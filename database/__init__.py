from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
import os

db: SQLAlchemy = SQLAlchemy()

def init_db(app: Flask):
    db.init_app(app)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    Migrate(app, db, directory=f"{BASE_DIR}/migrations")
    return db
