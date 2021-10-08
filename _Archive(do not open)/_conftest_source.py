import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help='Choose browser: chrome or firefox')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print('\nStart Chrome for tests')
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\nStart FF for tests')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name must be either chrome of firefox')
    yield browser
    browser.quit()