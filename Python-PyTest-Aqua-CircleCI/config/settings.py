import os
from dotenv import load_dotenv

# Завантажуємо змінні з файлу .env
load_dotenv()

TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("BASE_URL")
