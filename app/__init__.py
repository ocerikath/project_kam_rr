from flask import Flask
from flask_mail import Mail
from .models import db
from dotenv import load_dotenv
import os

mail = Mail()

def create_app():
    load_dotenv()  # ✅ Подгружаем .env

    app = Flask(__name__)

    # Настройка базы данных
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Настройки почты
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 465))
    app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', 'True').lower() == 'true'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

    db.init_app(app)
    mail.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
