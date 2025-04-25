"""Хранилище имени и цены товаров"""

class ProductInfo:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        """Добавляет продукт в хранилище"""
        self.products.append({
            'name': name.strip(),
            'price': price.strip()
        })
        return self

    def get_all_products(self):
        """Возвращает все продукты"""
        return self.products

    def get_last_product(self):
        """Возвращает последний добавленный продукт"""
        return self.products[-1] if self.products else None

    def compare_last_two(self):
        """сравнивает имя и цену последних 2 продуктов"""
        last = self.products[-1]
        prev = self.products[-2]
        assert last == prev
        print('Name and price OK') # если все ок


    def compare_last_two_price(self):
        """сравнивает цену последних 2 продуктов"""
        last_price = self.products[-1]['price']
        prev_price = self.products[-2]['price']
        assert last_price == prev_price
        print('Price OK') # если все ок
