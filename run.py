import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'HELLO FROM RAILWAY - FINALLY WORKS! 🎉'

@app.route('/health')
def health():
    return 'OK', 200

@app.route('/debug')
def debug():
    return f"""
    <h1>Debug Info</h1>
    <p>PORT: {os.environ.get('PORT')}</p>
    <p>RAILWAY_ENVIRONMENT: {os.environ.get('RAILWAY_ENVIRONMENT')}</p>
    <p>RAILWAY_PUBLIC_DOMAIN: {os.environ.get('RAILWAY_PUBLIC_DOMAIN')}</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"🚀 Starting Flask app on port {port}")
    print(f"🌐 Public URL: {os.environ.get('RAILWAY_PUBLIC_DOMAIN')}")
    app.run(host="0.0.0.0", port=port, debug=False)