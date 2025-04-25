import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.generated_random_data import *


class Basepage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    select_location = '//div[@data-test-header="location"]'
    input_location = '//input[@placeholder="Поиск города"]'
    """Локатор первого города который прописали в строке поиска"""
    my_city = '(//b[contains(@classname, "highlight")])[1]'
    button_catalog = '//button[@data-test-header="menu"]'
    button_pillows = "(//*[text()='Подушки'])[1]"
    button_all_pillows = "(//*[text()='Все подушки'])"
    main_word = "//*[text()='Подушки']"
    # Getters
    def get_button_select_location(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_location)))

    def get_input_location(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_location)))
    def get_my_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_city)))

    def get_button_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_catalog)))

    def get_button_pillows(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_pillows)))

    def get_button_all_pillows(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_all_pillows)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))



    # Actions
    def click_select_location(self):
        self.get_button_select_location().click()
        print('Click button select city')

    def input_city_location(self):
        self.get_input_location().send_keys(get_random_city())
        self.get_my_city().click()
        print('Input location')

    def click_button_catalog(self):
        self.get_button_catalog().click()
        print('Click button catalog')


    def click_pillows(self):
        self.get_button_pillows().click()
        print('Click button pilows')

    def click_all_pillows(self):
        self.get_button_all_pillows().click()
        print('Click button all pilows')




    # Methods
    """Жмем все подушки из каталога"""
    def select_all_pillows(self):
        self.get_current_url()
        self.click_select_location() # кликаем на выбор локации
        self.input_city_location() # заполняем
        time.sleep(2) # бывает сайт долго прогружается после выбора города
        self.click_button_catalog() # каталог
        time.sleep(3) # бывает каталог отображается с задержкой, но в дереве он есть и тест падает
        self.click_pillows() # подушки
        self.click_all_pillows()  # все подушки
        self.assert_word(self.get_main_word(), 'Подушки') # проверяем след страницу