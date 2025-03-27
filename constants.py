import os
from dotenv import load_dotenv

# Загрузка переменных из .env файла
load_dotenv()

# Константы для тестов
DEFAULT_LAST_NAME = os.environ.get("DEFAULT_LAST_NAME", "Meleaged")
