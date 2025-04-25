import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.generated_random_data import *


class AllPillows(Base):

    def __init__(self, driver, storage):
        super().__init__(driver)
        self.driver = driver
        self.storage = storage
    #Locators
    filter_adults = '//button[@data-cat_name="podushki"]'
    filter_anatomical = '//button[@data-cat_name="anatomicheskie"]'
    filter_on_the_back = '//button[@data-cat_name="na_spine"]'
    first_button_all_type = "(//*[text()='Показать все'])[1]"
    filter_size_pillows_11_15 = '//button[@data-cat_name="s_11_do_15"]' # размер от 11 до 15
    filter_rigidity_low = '//button[@data-cat_name="nizkaya"]' # жесткость
    filter_rigidity_medium = '//button[@data-cat_name="srednyaya"]'
    filter_min_price = "//input[@name='price' and @data-view='min']" # цена
    filter_max_price = "//input[@name='price' and @data-view='max']"
    filter_min_length = "//input[@name='dlina' and @data-view='min']" # длинна
    filter_max_length = "//input[@name='dlina' and @data-view='max']"
    filter_min_width = "//input[@name='shirina' and @data-view='min']" # ширина
    filter_max_width = "//input[@name='shirina' and @data-view='max']" #
    product_name = '(//div[@class="Product_type__7uFnL"])[1]'
    first_product_name = '(//div[@data-test-listing="product_name"])[1]' #имя первой подушки
    first_price = "(//div[@data-test-listing='new_price'])[1]" # цена первой подушки
    first_product_basket = "(//*[text()='В корзину'])[1]" # кнопка корзины для первой подушки
    window_number_tel = '(//button[@data-test-site="close_button"])'
    cart_word = "//*[text()='Итого']"


    # Getters
    def get_filter_adults(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_adults)))
    def get_filter_anatomical(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_anatomical)))
    def get_filter_on_the_back(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_on_the_back)))
    def get_first_button_all_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_button_all_type)))
    def get_filter_size_pillows_11_15(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_size_pillows_11_15)))
    def get_filter_rigidity_low(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_rigidity_low)))

    def get_filter_rigidity_medium(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_rigidity_medium)))
    def get_filter_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_min_price)))
    def get_filter_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_max_price)))
    def get_filter_min_length(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_min_length)))
    def get_filter_max_length(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_max_length)))
    def get_filter_min_width(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_min_width)))
    def get_filter_max_width(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_max_width)))

    def get_window_number_tel(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.window_number_tel)))
    def get_first_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_product_name)))
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name)))
    def get_first_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_price)))
    def get_first_product_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_product_basket)))

    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_word)))



    # Actions
    def click_filter_adults(self):
        self.get_filter_adults().click()
        print('Click filter_adults')
    def click_filter_anatomical(self):
        self.get_filter_anatomical().click()
        print('Click filter_anatomical')
    def click_filter_on_the_back(self):
        self.get_filter_on_the_back().click()
        print('Click filter_on_the_back')
    def click_first_button_all_type(self):
        self.get_first_button_all_type().click()
        print('Click first_button_all_type')
    def click_filter_size_pillows_11_15(self):
        self.get_filter_size_pillows_11_15().click()
        print('Click filter_size_pillows_11_15')
    def click_filter_rigidity_low(self):
        self.get_filter_rigidity_low().click()
        print('Click filter_rigidity_low')

    def click_filter_rigidity_medium(self):
        self.get_filter_rigidity_medium().click()
        print('Click filter_rigidity_medium')
    def click_filter_min_price(self):
        price = get_random_prices()
        self.get_filter_min_price().send_keys(price['min'])
        print('Click filter_min_price')
    def click_filter_max_price(self):
        price = get_random_prices()
        self.get_filter_max_price().send_keys(price['max'])
        print('Click filter_max_price')
    def click_filter_min_length(self):
        leingt = get_random_length()
        self.get_filter_min_length().send_keys(leingt['min'])
        print('Click filter_min_length')
    def click_filter_max_length(self):
        leingt = get_random_length()
        self.get_filter_max_length().send_keys(leingt['max'])
        print('Click filter_max_length')
    def click_filter_min_width(self):
        width = get_random_width()
        self.get_filter_min_width().send_keys(width['min'])
        print('Click filter_min_width')
    def click_filter_max_width(self):
        width = get_random_width()
        self.get_filter_max_width().send_keys(width['max'])
        print('Click filter_max_width')

    """Бывает появляется после верхнего действия окно с указанием номера, его еще можно закрыть кликнув в любую область"""

    def close_window_number_tel(self):
        try:
            self.get_window_number_tel().click()
            print('Window nubmer tel closed')
        except:
            print('Window nubmer tel is not')

    def parser_info_first_product(self):
        self.perform_on_element(self.product_name)
        name = f'{self.get_product_name().text} {self.get_first_product_name().text}'
        print(name)
        price = self.get_first_price().text
        self.storage.add_product(name, price)
        print(f"Print product: {name}, Price: {price}")
        return self.storage

    def click_first_product_basket(self):
        # self.perform_on_element(self.first_product_basket)
        self.get_first_product_basket().click()
        print('Click first_product_button_basket')





    # Methods
    def select_first_product_with_filter(self):
        self.get_current_url()
        self.click_filter_adults()
        time.sleep(1) # бывает долго разблокировка кнопок происходит после выбора первого фильтра
        self.click_filter_anatomical()
        self.click_filter_on_the_back()
        self.click_first_button_all_type()
        self.click_filter_size_pillows_11_15()
        self.click_filter_rigidity_medium()
        self.click_filter_min_price()
        self.click_filter_max_price()
        self.click_filter_min_length()
        self.click_filter_max_length()
        self.click_filter_min_width()
        self.click_filter_max_width()
        self.close_window_number_tel() # бывает всплывает, если всплывет то метод закроет его
        self.parser_info_first_product() # парсим имя и цену продукта
        self.click_first_product_basket() ## навигируемся и кликаем в корзину
        self.assert_word(self.get_cart_word(), 'Итого') #чекаем переход в корзину