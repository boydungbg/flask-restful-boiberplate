import logging
import os
from logging.handlers import TimedRotatingFileHandler
from flask import Flask


def config_log(app: Flask):
    BASE_DIR = os.curdir

    # Create a TimedRotatingFileHandler
    log_handler = TimedRotatingFileHandler(
        filename=f"{BASE_DIR}/storage/logs/app.log",
        when="midnight",
        interval=1,
        backupCount=7,
    )

    # Set the log format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    log_handler.setFormatter(formatter)

    # Set the log level
    log_handler.setLevel(logging.INFO)

    # Add the handler to the Flask app's logger
    app.logger.addHandler(log_handler)
