from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from routes import ai_routes
from middleware import sanitize_prompt

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

app = Flask(__name__)
limiter = Limiter(key_func=get_remote_address, default_limits=["30 per minute"])
limiter.init_app(app)
app.register_blueprint(ai_routes.bp)
app.before_request(sanitize_prompt)

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "frame-ancestors 'none';"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
