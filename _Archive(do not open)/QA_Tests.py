import time, math, os, unittest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

class TestCases(unittest.TestCase):
	def test1(self):
		try:
			browser = webdriver.Chrome()
			browser.implicitly_wait(5)
			browser.get('https://suninjuly.github.io/registration1.html')
			browser.find_element_by_xpath('//input[contains(@placeholder, "first name")]').send_keys('First name')
			browser.find_element_by_xpath('//input[contains(@placeholder, "last name")]').send_keys('Second name')
			browser.find_element_by_xpath('//input[contains(@placeholder, "email")]').send_keys('email@test.com')
			browser.find_element_by_css_selector("[type='submit']").click()
			WebDriverWait(browser, 5).until(EC.url_contains('result'))
			self.assertEqual(browser.find_element(By.TAG_NAME, 'h1').text, 'Congratulations! You have successfully registered!', 'You are not registered')
		finally:
			browser.quit()
	def test2(self):
		try:
			browser = webdriver.Chrome()
			browser.implicitly_wait(5)
			browser.get('http://suninjuly.github.io/registration2.html')
			browser.find_element_by_xpath('//input[contains(@placeholder, "your name")]').send_keys('First name')
			browser.find_element_by_xpath('//input[contains(@placeholder, "first name")]').send_keys('Second name')
			browser.find_element_by_xpath('//input[contains(@placeholder, "email")]').send_keys('email@test.com')
			browser.find_element_by_css_selector("[type='submit']").click()
			WebDriverWait(browser, 5).until(EC.url_contains('result'))
			self.assertEqual(browser.find_element(By.TAG_NAME, 'h1').text, 'Congratulations! You have successfully registered!', 'You are not registered')
		finally:
			browser.quit()