from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage, ProductPageLocators, PromoPagesLocators
import time, pytest

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_to_cart()
    page.solve_alert_task()
    added_product_name = page.get_name_of_added_item()
    assert product_name == added_product_name
    basket_price = page.get_price_of_basket()
    assert product_price == basket_price


@pytest.mark.promo
@pytest.mark.parametrize('promo_num', range(10))
def test_promo_pages(browser, promo_num):
    link = PromoPagesLocators.PROMO_LINK + str(promo_num)
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)