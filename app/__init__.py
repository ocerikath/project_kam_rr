from flask import Flask
from .models import db
from flask_mail import Mail
from config import Config
import os
from dotenv import load_dotenv

mail = Mail()

def create_app():
    # Загружаем .env только для локальной разработки
    if os.environ.get("RAILWAY_ENVIRONMENT") is None:  # Более надежная проверка
        load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализируем расширения
    db.init_app(app)
    mail.init_app(app)

    # Импортируем и регистрируем blueprint
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Создаем таблицы при запуске
    with app.app_context():
        db.create_all()

    return app