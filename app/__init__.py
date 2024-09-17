"""
This module initializes the Flask application and sets up Swagger for API documentation.
"""
import os
from dotenv import load_dotenv
from flask import Flask
from flasgger import Swagger
from config.log_config import configure_logging

# Load environment variables from .env file
load_dotenv()

# Create Flask application
app = Flask(__name__)

# Setting up Swagger configuration for API documentation
app.config['SWAGGER'] = {
    'title': 'Avatar Maker API',
    'description': 'API for generating personalized avatars.'
}

# Temp and Log directories configuration
app.config['RESULT_FOLDER'] = os.getenv('RESULT_FOLDER', 'results')
app.config['LOG_DIR'] = os.getenv('LOG_DIR', 'logs')

# Create directories if they don't exist
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)
os.makedirs(app.config['LOG_DIR'], exist_ok=True)

# Initialize Swagger
swagger = Swagger(app)

# Configure logging
configure_logging(app)

# Import routes at the end
from app import routes
