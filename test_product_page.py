from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage, ProductPageLocators, PromoPagesLocators
import time, pytest

@pytest.mark.skip
@pytest.mark.parametrize('promo_num', [0, 1, 2, 3, 4, 5, 6,
                                       pytest.param('bugged promo number', marks=pytest.mark.xfail),
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
    assert product_name == added_product_name
    basket_price = page.get_price_of_basket(ProductPageLocators.BASKET_PRICE)
    assert product_price == basket_price

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.add_to_cart()
    page.solve_alert_task()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_MESSAGE)
    #time.sleep(3)

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_MESSAGE)

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.add_to_cart()
    page.solve_alert_task()
    assert page.is_disappeared(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_MESSAGE)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()