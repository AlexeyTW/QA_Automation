import time, math, os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)
try:
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
	browser.find_element_by_id('book').click()
	input_value = browser.find_element_by_id('input_value').text
	browser.find_element_by_id('answer').send_keys(calc(input_value))
	browser.find_element_by_id('solve').click()
	answer = browser.switch_to.alert.text
	print(answer)
finally:
	browser.quit()