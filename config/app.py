import os


class AppConfig:
    app_development = os.getenv("APP_DEBUG", "true")
    app_port = os.getenv("APP_PORT", 5000)
    app_secret_key = os.getenv("APP_SECRET_KEY", "")
