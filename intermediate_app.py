from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'test-key')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-test-key')

# Database configuration (with graceful fallback)
try:
    DATABASE_URL = os.getenv('DATABASE_URL')
    if not DATABASE_URL:
        DATABASE_USER = os.getenv('DATABASE_USER', 'postgres')
        DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'postgres')
        DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
        DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
        DATABASE_NAME = os.getenv('DATABASE_NAME', 'MyPortalDb')
        DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database
    db = SQLAlchemy(app)
    print("Database initialized successfully")
    
except Exception as e:
    print(f"Database initialization skipped: {e}")
    db = None

# Initialize other extensions
jwt = JWTManager(app)
CORS(app)

@app.route('/')
def hello():
    return jsonify({'message': 'Intermediate Flask App - Database and Auth Working!'})

@app.route('/health')
def health():
    db_status = "connected" if db else "not configured"
    return jsonify({
        'status': 'healthy', 
        'service': 'internship-portal',
        'database': db_status,
        'components': ['flask', 'sqlalchemy', 'jwt', 'cors']
    })

@app.route('/test-db')
def test_db():
    if db:
        try:
            # Test database connection
            result = db.engine.execute('SELECT 1')
            return jsonify({'database': 'connected', 'test_query': 'success'})
        except Exception as e:
            return jsonify({'database': 'error', 'message': str(e)})
    else:
        return jsonify({'database': 'not configured'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)