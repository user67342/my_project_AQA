import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage
from utilities.generated_random_data import *


class OrderPage(CartPage):

    def __init__(self, driver, storage):
        super().__init__(driver, storage)
        self.driver = driver

    #Locators
    total_price  = '//span[@data-test-checkout="price_total"]'
    phone = '//input[@id="phone"]'
    name = '//input[@id="name"]'
    email = '//input[@id="email"]'
    self_pickup = "//*[text()='Самовывоз со склада или из магазина Аскона']"
    pickup = '//img[@src="/local/templates/assets//img/map/pickupStore-disabled.png"]'
    map_pickup = '//button[@data-test-checkout_modal_pickup="map_button"]'
    place_an_order = '//button[@data-test-checkout="buy"]'
    cash_on_delivery = '//div[@data-test-checkout_payment="При получении"]'
    succes_order_word = "//*[text()='Номер вашего заказа']"
    """Когда я закончил писать проект, на сайте ввели обязательную верификацию по номеру телефона"""
    """Ранее заказ можно  было оформить без верификации"""
    new_succes_word = "//*[text()='Подтвердите номер телефона']"


    # Getters
    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_self_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.self_pickup)))

    def get_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup)))


    def get_map_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.map_pickup)))

    def get_cash_on_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cash_on_delivery)))

    def get_place_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.place_an_order)))

    def get_success_order_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.succes_order_word)))

    def get_new_success_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_succes_word)))


    # Actions

    def parser_total_price(self):
        price = self.get_total_price().text
        self.storage.add_product('Имя', price) # добавляем спарсенную цену

    def input_phone(self):
        self.get_phone().click()
        self.get_phone().send_keys(get_random_phone())
        print('input phone')

    def input_name(self):
        self.get_name().send_keys(get_random_name())
        print('input name')

    def input_email(self):
        self.get_email().send_keys(get_random_email())
        print('input email')

    def click_self_pickup(self):
        self.get_self_pickup().click()
        print('Click self pickup')

    def click_pickup(self):
        self.get_pickup().click()
        print('Click pickup')

    def click_map_pickup(self):
        self.get_map_pickup().click()
        print('Click map pickup')

    def click_cash_on_delivery(self):
        self.perform_on_element(self.cash_on_delivery)
        time.sleep(1) # бывает нужна
        self.get_cash_on_delivery().click()
        print('Click cash on delivery')

    def click_place_an_order(self):
        self.get_place_an_order().click()
        print('Click place_an_order')




    # Methods
    """Жмем все подушки из каталога"""
    def place_order(self):
        self.get_current_url()
        self.input_phone()
        self.input_name()
        self.input_email()
        self.click_self_pickup() # изменить адрес на самовывоз
        self.click_pickup() # клик на первый склада
        self.click_map_pickup() # выбрать первый склад
        self.parser_total_price()  # парсим цену
        self.storage.compare_last_two_price() # сравниваем цену с предыдущей
        self.click_cash_on_delivery() # жмем оплатить при получении
        self.click_place_an_order() # кликаем оформить
        self.assert_url('/cabinet/order/')
        # self.assert_word(self.get_success_order_word(), 'Номер вашего заказа')  # проверяем поле успешного оформления заказа


        """Когда я закончил писать проект, на сайте ввели обязательную верификацию по номеру телефона"""
        """Ранее заказ можно  было оформить без верификации"""
        self.assert_word(self.get_new_success_word(), 'Подтвердите номер телефона')  #
        self.get_screenshot() # делаем скрин