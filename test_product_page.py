from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage, ProductPageLocators, PromoPagesLocators
from .pages.locators import BasePageLocators, MainPageLocators
import time, pytest


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.add_to_cart()
    page.solve_alert_task()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_MESSAGE)
    #time.sleep(3)

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.add_to_cart()
    page.solve_alert_task()
    assert page.is_disappeared(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_MESSAGE)

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.check_basket_has_no_products()
    assert page.check_message_basket_is_empty()

@pytest.mark.skip
class TestUserAddToBasketFromProductPage:

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_MESSAGE)

    #@pytest.mark.parametrize('promo_num', [0, 1, 2, 3, 4, 5, 6,
     #                                      pytest.param('bugged promo number', marks=pytest.mark.xfail),
      #                                     8, 9])

    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.PRODUCT_LINK
        page = ProductPage(browser, link)
        page.open()
        product_name = page.get_product_name(ProductPageLocators.PRODUCT_NAME)
        product_price = page.get_product_price(ProductPageLocators.PRODUCT_PRICE)
        page.add_to_cart()
        page.solve_alert_task()
        added_product_name = page.get_name_of_added_item(ProductPageLocators.PRODUCT_NAME)
        assert product_name == added_product_name
        basket_price = page.get_price_of_basket(ProductPageLocators.BASKET_PRICE)
        assert product_price == basket_price

def test_register_user(browser):
    link = MainPageLocators.MAIN_PAGE_LINK
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user('em@tsh.con', 'HSYd73djsd9')
    time.sleep(3)