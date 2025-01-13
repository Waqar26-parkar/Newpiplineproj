from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Configurations
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
app.config['PORT'] = int(os.getenv('PORT', 9090))


# Routes
@app.route('/')
def home():
    return "Welcome to the Advanced Flask App!"

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Healthy"}), 200

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return jsonify({"echo": data}), 200

@app.route('/api/env', methods=['GET'])
def environment():
    return jsonify({"environment": dict(os.environ)}), 200

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=app.config['PORT'], debug=app.config['DEBUG'])
    except Exception as e:
        print(f"Error starting the app: {e}")
