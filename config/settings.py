import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    #Окружение
    ENV = os.getenv('ENVIRONMENT', 'prod')  # Значение по умолчанию - 'prod'

    #URL
    BASE_URLS = {
        'local': 'http://localhost:7080',
        'prod': 'https://the-internet.herokuapp.com'
    }
    BASE_URL = BASE_URLS[ENV]  # Автоматический выбор URL по окружению

    #Браузеры
    BROWSER = os.getenv('BROWSER', 'chrome')  # по умолчанию 'chrome'
    WINDOW_SIZE = (os.getenv('WINDOW_WIDTH', '1920'),  # Ширина по умолчанию 1920
                os.getenv('WINDOW_HEIGHT', '1080')) # Длина по умолчанию 1080

    #Настройки тестов
    COUNT_RESTARTS = int(os.getenv('RETRY_COUNT', '2'))  # Повторные попытки при падении. По умолчанию 2 попытки.

settings = Settings()