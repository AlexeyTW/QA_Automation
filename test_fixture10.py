import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

class TestMainPage1:
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        print('Smoke test')
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('Regression test')
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason='Fixing right now')
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        print('Skipped test')
        browser.get(link)
        browser.find_element_by_css_selector("input.btn.btn-default")