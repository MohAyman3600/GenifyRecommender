import os
from app import create_app
from dotenv import load_dotenv

load_dotenv()


app = create_app(config_name=os.getenv('ENV_PROD'))

if __name__ == '__main__':
    app.run()
