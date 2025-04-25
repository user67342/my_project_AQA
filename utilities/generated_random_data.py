import random
from faker import Faker

"""Генератор рандомных данных"""

def get_random_city():
    return random.choice(['Сочи', 'Ульяновск', 'Воскресенск'])

def get_random_prices():
    """рандомные цены"""
    return {
        'min': random.randint(1000, 2000),
        'max': random.randint(5000, 6000)
    }

def get_random_length():
    """рандомная длинна"""
    return {
        'min': random.randint(22, 40),
        'max': random.randint(100, 125)
    }

def get_random_width():
    """рандомная ширина"""
    return {
        'min': random.randint(21, 30),
        'max': random.randint(60, 72)
    }

def get_random_name():
    """Рандомное имя"""
    fak = Faker('ru_RU')
    name = fak.first_name()
    return name

def get_random_phone():
    """Генерирует случайный телефонный номер в формате 910"""
    fak = Faker('ru_RU')
    # Генерируем номер, начинающийся с 91 и 7 случайных цифр
    phone = '910' + fak.numerify(text='#######')
    return phone

def get_random_email():
    """Рандомный email"""
    fak = Faker('en_US')
    email = fak.email(domain='inbox.ru')
    return email