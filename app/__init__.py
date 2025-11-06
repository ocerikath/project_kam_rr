from flask import Flask
from .models import db
from flask_mail import Mail
from config import Config
import os
from dotenv import load_dotenv

mail = Mail()

def create_app():
    # Загружаем .env только для локальной разработки
    if os.environ.get("RAILWAY_ENVIRONMENT") is None:
        load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализируем расширения
    db.init_app(app)
    mail.init_app(app)

    # ВРЕМЕННО закомментируем создание таблиц
    # with app.app_context():
    #     try:
    #         db.engine.connect()
    #         print("✅ Database connection successful")
    #         db.create_all()  # Закомментируем эту строку
    #     except Exception as e:
    #         print(f"❌ Database connection failed: {e}")

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app