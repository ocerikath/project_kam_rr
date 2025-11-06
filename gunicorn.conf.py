# gunicorn.conf.py
import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"
workers = 1
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 5

# Отключаем sendfile для избежания ошибок
sendfile = False

# Логирование
accesslog = "-"
errorlog = "-"
loglevel = "info"