import os
import sys

print("=" * 50)
print("🚀 STARTING APPLICATION")
print("=" * 50)

# Выводим все переменные окружения
print("📋 ENVIRONMENT VARIABLES:")
for key, value in os.environ.items():
    if any(x in key for x in ['PORT', 'RAILWAY', 'DATABASE']):
        print(f"   {key}: {value}")

try:
    from flask import Flask
    print("✅ Flask imported successfully")
except Exception as e:
    print(f"❌ Flask import failed: {e}")
    sys.exit(1)

app = Flask(__name__)
print("✅ Flask app created")

@app.route('/')
def hello():
    print("📥 GET / request received")
    return 'HELLO FROM RAILWAY - FINALLY WORKS! 🎉'

@app.route('/health')
def health():
    print("📥 GET /health request received")
    return 'OK', 200

@app.route('/debug')
def debug():
    port = os.environ.get('PORT')
    railway_env = os.environ.get('RAILWAY_ENVIRONMENT')
    public_domain = os.environ.get('RAILWAY_PUBLIC_DOMAIN')
    
    print(f"📥 GET /debug request received - Port: {port}")
    
    return f"""
    <h1>Debug Info</h1>
    <p>PORT: {port}</p>
    <p>RAILWAY_ENVIRONMENT: {railway_env}</p>
    <p>RAILWAY_PUBLIC_DOMAIN: {public_domain}</p>
    <p>Python version: {sys.version}</p>
    """

if __name__ == "__main__":
    # Railway дает порт в переменной PORT, обычно это 8080 или подобный
    port = int(os.environ.get("PORT", 8080))
    print(f"🔧 Configuration:")
    print(f"   - Port: {port}")
    print(f"   - Public URL: {os.environ.get('RAILWAY_PUBLIC_DOMAIN')}")
    print(f"   - Environment: {os.environ.get('RAILWAY_ENVIRONMENT')}")
    
    print(f"🚀 Starting Flask app on 0.0.0.0:{port}")
    
    try:
        app.run(host="0.0.0.0", port=port, debug=False)
        print("✅ Flask app started successfully")
    except Exception as e:
        print(f"❌ Failed to start Flask: {e}")
        sys.exit(1)