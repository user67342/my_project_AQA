import time
from pages.all_pillows_page import AllPillows
from pages.base_page import Basepage
from conftest import set_up, set_group
from pages.cart_page import CartPage
from pages.order_page import OrderPage
from utilities.data_info_product import ProductInfo


# @pytest.mark.order(2)
def test_buy_product_1(set_up):
    """Берем из set_up настройки браузера"""
    driver = set_up

    print('Start Test 1')
    first_step = Basepage(driver)
    first_step.select_all_pillows()
    storage = ProductInfo()
    two_step = AllPillows(driver, storage)
    two_step.select_first_product_with_filter()
    three_step = CartPage(driver, storage)
    three_step.select_continue()
    four_step = OrderPage(driver, storage)
    four_step.place_order()



    driver.quit()