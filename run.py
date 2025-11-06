import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from Railway!'

@app.route('/health')
def health():
    return 'OK', 200

@app.route('/test')
def test():
    return f"Port: {os.environ.get('PORT')}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway использует 8080
    app.run(host="0.0.0.0", port=port, debug=False)