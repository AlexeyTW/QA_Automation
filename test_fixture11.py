import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

class TestClass:

    @pytest.mark.parametrize('language', ['ru', 'en-gb'])
    def test_guest_should_see_login_link(self, browser, language):
        link = f'https://selenium1py.pythonanywhere.com/{language}/'
        print(link)
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")