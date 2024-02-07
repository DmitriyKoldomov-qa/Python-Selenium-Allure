# импортируем модули и отдельные классы
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

url = "https://testqastudio.me/"

@pytest.fixture(scope="session") # указываем что фикстура работает в рамках всей тестовой сессии
# Описываем фикстуру_
def browser():
    """
    Main fixture
    """
	# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url=url)
    yield driver # передаем в нашу тестовую функцию
    driver.quit() # если функция штатно или не штатно завершилась, закрывем драйвер