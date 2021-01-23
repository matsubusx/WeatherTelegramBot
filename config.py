import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

variables = {
    'TG_TOKEN': os.environ['TG_TOKEN'],
    'APP_ID': os.environ['APP_ID']
}