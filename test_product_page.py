from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage, ProductPageLocators, PromoPagesLocators
from .pages.locators import BasePageLocators, MainPageLocators
import time, pytest, random

@pytest.mark.need_review
@pytest.mark.parametrize('promo_num', [0, 1, 2, 3, 4, 5, 6,
                                       pytest.param('bugged promo number', marks=pytest.mark.xfail(reason='This is the bugged promo page. Text is xpassed')),
                                       8, 9])
def test_guest_can_add_product_to_basket(browser, promo_num):
    link = PromoPagesLocators.PROMO_LINK + str(promo_num)
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name(ProductPageLocators.PRODUCT_NAME)
    product_price = page.get_product_price(ProductPageLocators.PRODUCT_PRICE)
    page.add_to_cart()
    page.solve_alert_task()
    added_product_name = page.get_name_of_added_item(ProductPageLocators.PRODUCT_NAME)
    page.check_equality_of_values(product_name, added_product_name)
    basket_price = page.get_price_of_basket(ProductPageLocators.BASKET_PRICE)
    page.check_equality_of_values(product_price, basket_price)

@pytest.mark.xfail(reason='This test should be xfailed because guest can see success message after adding item to the cart')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.add_to_cart()
    page.solve_alert_task()
    page.check_object_not_present(ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_MESSAGE)

@pytest.mark.xfail(reason='This test should be xfailed')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.add_to_cart()
    page.solve_alert_task()
    page.check_object_not_present(ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_MESSAGE)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.check_basket_has_no_products()
    page.check_message_basket_is_empty()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + '@em.com', 'HDHSY7f8fh7')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
        page.open()
        page.check_object_not_present(ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_MESSAGE)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.PRODUCT_LINK
        page = ProductPage(browser, link)
        page.open()
        product_name = page.get_product_name(ProductPageLocators.PRODUCT_NAME)
        product_price = page.get_product_price(ProductPageLocators.PRODUCT_PRICE)
        page.add_to_cart()
        page.solve_alert_task()
        added_product_name = page.get_name_of_added_item(ProductPageLocators.PRODUCT_NAME)
        page.check_equality_of_values(product_name, added_product_name)
        basket_price = page.get_price_of_basket(ProductPageLocators.BASKET_PRICE)
        page.check_equality_of_values(product_price, basket_price)