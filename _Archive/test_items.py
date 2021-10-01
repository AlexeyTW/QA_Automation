import pytest
from selenium.webdriver import Chrome

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_page_contains_bin_button(browser):
	browser.get(link)
	assert browser.find_element_by_css_selector("button[type='submit'][value]").is_enabled()


