import os

from flask import Flask


class DatabaseConfig:

    db_connection = os.getenv("DB_CONNECTION", "mysql")

    mysql_connection = dict(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 3306),
        database=os.getenv("DB_DATABASE", "python_database"),
        username=os.getenv("DB_USERNAME", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
    )

    def config_database(app: Flask):
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"mysql+pymysql://{DatabaseConfig.mysql_connection['username']}:{DatabaseConfig.mysql_connection['password']}@{DatabaseConfig.mysql_connection['host']}:{DatabaseConfig.mysql_connection['port']}/{DatabaseConfig.mysql_connection['database']}"
        )
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
