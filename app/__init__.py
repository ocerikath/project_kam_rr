import os
from flask import Flask, send_from_directory
from .models import db
from flask_mail import Mail
from config import Config
from dotenv import load_dotenv

mail = Mail()

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
            print("✅ Database tables created successfully")
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            print("⚠️ Continuing without database...")

    # -------------------------------
    # Маршруты для SEO и подтверждения
    # -------------------------------
    @app.route('/robots.txt')
    def robots():
        return send_from_directory(app.root_path, 'robots.txt')

    @app.route('/sitemap.xml')
    def sitemap():
        return send_from_directory(app.root_path, 'sitemap.xml')

    # Яндекс HTML подтверждение
    @app.route('/yandex_6a7ddba0e90f0afc.html')
    def yandex_verification():
        return send_from_directory(app.root_path, 'yandex_6a7ddba0e90f0afc.html')

    return app
