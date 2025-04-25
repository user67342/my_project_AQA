import os
import time

from selenium_stealth import stealth
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
@pytest.fixture()
def set_up():
    print("\nЗапуск теста")  # перед тестом
    url = 'https://www.askona.ru//'

    chrome_options = Options()

    """Режим headless"""
    chrome_options.add_argument("--headless")

    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")  # Отключает информационные бары
    chrome_options.add_argument("--disable-popup-blocking")  # Блокировка всплывающих окон
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2,  # Блокировать все уведомления
        "profile.managed_default_content_settings.notifications": 2
    })
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--incognito")


    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, 'utilities', 'chromedriver.exe')
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.execute_script("""
        var popup = document.querySelector('.popup-selector');
        if (popup) popup.remove();
    """)
    driver.maximize_window()
    driver.get(url)
    yield driver
    print("\nТест завершен!")    #после теста

    # python - m pytest - s - v test_by_product.py

@pytest.fixture(scope="module")
def set_group():
    print("\nEnter sytstem")    #перед тестом
    yield    #сам тест
    print("\Exit system")    #после теста