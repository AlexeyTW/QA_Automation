from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage, ProductPageLocators
import time

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.add_to_cart()
    page.solve_alert_task()

    time.sleep(300)