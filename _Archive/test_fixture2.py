import pytest
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture
def browser():
    return webdriver.Chrome()

class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_id('login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    return browser

class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")