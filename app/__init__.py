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

    return app

# robots.txt
@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(app.root_path, ''), 'robots.txt')

# sitemap.xml
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, ''), 'sitemap.xml')