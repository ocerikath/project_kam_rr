import os
from flask import Flask, send_from_directory
from .models import db
from flask_mail import Mail
from config import Config
from dotenv import load_dotenv
import requests

mail = Mail()
load_dotenv()

def send_telegram(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not token or not chat_id:
        print(f"❌ Ошибка: Токен ({token}) или Chat ID ({chat_id}) не найдены!")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}
    
    try:
        response = requests.post(url, data=data)
        # Это самое важное — смотрим, что ответил Телеграм
        print(f"📡 TG Status: {response.status_code} | Response: {response.text}")
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Ошибка запроса к Telegram: {e}")

def create_app():
    # Загружаем .env только для локальной разработки
    if os.environ.get("RAILWAY_ENVIRONMENT") is None:
        load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # Отладочная информация
    print(f"Database URL: {app.config.get('SQLALCHEMY_DATABASE_URI', 'Not set')}")

    # Инициализируем расширения
    db.init_app(app)
    mail.init_app(app)

    # Импортируем и регистрируем blueprint
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Создаем таблицы при запуске (с обработкой ошибок)
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully")
        except Exception as e:
            print(f"Database connection failed: {e}")
            print("Continuing without database...")

    # -------------------------------
    # Маршруты для SEO и подтверждения
    # -------------------------------
    # robots.txt
    @app.route('/robots.txt')
    def robots():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt')

    # sitemap.xml
    @app.route('/sitemap.xml')
    def sitemap():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')

    # Яндекс подтверждение
    @app.route('/yandex_6a7ddba0e90f0afc.html')
    def yandex_verification():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'yandex_6a7ddba0e90f0afc.html')

    return app

