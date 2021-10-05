from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage, ProductPageLocators, PromoPagesLocators
import time, pytest


@pytest.mark.parametrize('promo_num', [0, 1, 2, 3, 4, 5, 6,
                                       pytest.param('bugged promo number', marks=pytest.mark.xfail),
                                       8, 9])
def test_guest_can_add_product_to_basket(browser, promo_num):
    link = PromoPagesLocators.PROMO_LINK + str(promo_num)
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_to_cart()
    page.solve_alert_task()
    added_product_name = page.get_name_of_added_item()
    assert product_name == added_product_name
    basket_price = page.get_price_of_basket()
    assert product_price == basket_price