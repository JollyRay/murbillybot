import os
from dotenv import load_dotenv

load_dotenv()

DIR_PATH = os.path.abspath('.')
RESOURCE_PATH = os.path.join(DIR_PATH, 'resource')

BOT_TOKEN = os.getenv('BOT_TOKEN')