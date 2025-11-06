from app import create_app
from app.models import db
import os

app = create_app()

if __name__ == "__main__":
    # Этот блок выполняется только при прямом запуске python run.py
    # На Railway приложение запускается через gunicorn, поэтому этот код не выполняется
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)