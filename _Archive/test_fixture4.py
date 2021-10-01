import pytest
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        print('start test 1')
        browser.get(link)
        browser.find_element_by_id('login_link')
        print('finish test 1')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('start test 2')
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')
        print('finish test 2')