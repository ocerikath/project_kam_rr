import os
from app import create_app
from app.models import db

app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway сам подставит порт
    app.run(host="0.0.0.0", port=port, debug=False)
