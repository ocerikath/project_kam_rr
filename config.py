import os
import logging

class Config:

    database_url = os.environ.get("DATABASE_PUBLIC_URL") or os.environ.get("DATABASE_URL")
    

    if database_url:
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql+psycopg://", 1)
        elif database_url.startswith("postgresql://"):

            database_url = database_url.replace("postgresql://", "postgresql+psycopg://", 1)
    
    SQLALCHEMY_DATABASE_URI = database_url or "postgresql+psycopg://postgres:urdatabase@localhost:port/name"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 465))
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", "True").lower() == "true"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")

    # Логирование
    LOG_LEVEL = logging.INFO