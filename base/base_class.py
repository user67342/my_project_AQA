import os
import datetime
from urllib.parse import urlparse

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    """Навигация к элементу"""
    def perform_on_element(self, element):
        the_element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, element)))
        action = ActionChains(self.driver)
        action.move_to_element(the_element).perform()
        print('Сделали навигацию к элементу')


    """Получаем текущий URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Текущий url: {get_url}')

    """Метод проверки слов"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')


    """Метод создания скриншотов - заработало только так"""
    def get_screenshot(self):
        # Получаем абсолютный путь к корню проекта
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screen_dir = os.path.join(project_root, 'screen')
        # Создаем папку screen если её нет
        os.makedirs(screen_dir, exist_ok=True)
        # Формируем имя файла
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = os.path.join(screen_dir, f'screenshot {now_date}.png')
        # Сохраняем скриншот
        self.driver.save_screenshot(name_screenshot)
        print(f"Скриншот сохранён: screenshot {now_date}")


    """Method проверки URL"""
    def assert_url(self, result):
        current_url = self.driver.current_url
        parsed_url = urlparse(current_url)
        current_path = parsed_url.path  # Получаем только путь
        assert current_path == result
        print('URL corrected')
