from flask import Flask, jsonify
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Basic configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'test-key')

@app.route('/')
def hello():
    return jsonify({'message': 'Hello World - Minimal Flask App Working!'})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'internship-portal'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)