import os
from app import create_app

app = create_app()  # Gunicorn использует эту переменную

# Только для локальной разработки
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
