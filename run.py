from server import create_app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the configuration from the environment variable
config_name = os.getenv('FLASK_CONFIG') or 'dev'

app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)