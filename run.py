from server import create_app
from dotenv import load_dotenv
import os

load_dotenv()
config_name = os.getenv('FLASK_CONFIG', 'dev')
app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)