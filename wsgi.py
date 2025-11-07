from app import create_app
from app.models import db
import os
from flask import Flask, redirect, request

@app.before_request
def redirect_to_www():
    host = request.host
    # Проверяем, что 'www.' нет в адресе и что это не локальный запуск
    if not host.startswith('www.') and not host.startswith('localhost'):
        new_url = request.url.replace('//', '//www.', 1)
        return redirect(new_url, code=301)
        
app = create_app()

if __name__ == "__main__":
    # Этот блок выполняется только при прямом запуске python run.py
    # На Railway приложение запускается через gunicorn, поэтому этот код не выполняется
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)