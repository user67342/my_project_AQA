from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.all_pillows_page import AllPillows


class CartPage(AllPillows):

    def __init__(self, driver, storage):
        super().__init__(driver, storage)
        self.driver = driver

    #Locators
    name_product = '//a[@data-test-basket="product_name"]'
    price_product = '//div[@data-test-basket="new_price"]'
    checkout = '//button[@data-test-basket="to_checkout"]'
    total_price = '//span[@data-test-basket="total_price"]'
    order_word = '//h1[@data-test-checkout="title"]'

    # Getters
    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_order_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_word)))

    # Actions
    def parser_info_in_cart(self):
        name = self.get_name_product().text
        price = self.get_price_product().text
        self.storage.add_product(name, price)
        print(f"Print product: {name}, Price: {price}")
        return self.storage


    def parser_total_price_and_name(self):
        name = self.get_name_product().text
        price = self.get_total_price().text
        self.storage.add_product(name, price)
        print(f"Print product: {name}, Price: {price}")

    def click_checkout(self):
        self.get_checkout().click()
        print('Click checkout')



    # Methods
    """Жмем все подушки из каталога"""
    def select_continue(self):
        self.get_current_url()
        self.parser_info_in_cart()
        self.storage.compare_last_two() # проверяем название и цену в корзине с данными из каталога
        self.parser_total_price_and_name() # подгружаем в наш storage снова имя товара и итоговую цену
        self.storage.compare_last_two() # проверяем еще раз название и итоговую цену в корзине
        self.click_checkout() # жмем продолжить
        self.assert_word(self.get_order_word(), 'Оформление заказа')
