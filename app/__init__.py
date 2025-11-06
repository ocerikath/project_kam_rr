from flask import Flask
from .models import db
from flask_mail import Mail
from config import Config

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
