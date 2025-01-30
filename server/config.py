import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() in ['true', '1', 't']
    CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')  # Can be changed to 'redis' or other types
    RATE_LIMIT = os.getenv('RATE_LIMIT', '100 per hour')  # Example rate limit
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_unicode_ci'
        }
    }

class DevelopmentConfig(Config):
    DEBUG = os.getenv('DEBUG', 'True').lower() in ['true', '1', 't']
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'mysql+mysqlconnector://root:@localhost/advanced_api_development_dev')

class TestingConfig(Config):
    TESTING = os.getenv('TESTING', 'True').lower() in ['true', '1', 't']
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_TEST', 'sqlite:///test.db')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_PROD', 'mysql+mysqlconnector://root:@localhost/advanced_api_development')

config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}