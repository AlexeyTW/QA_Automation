import time

from selenium.webdriver import Chrome
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')
box = browser.find_element_by_id('treasure')
val = box.get_attribute('valuex')
ans = calc(val)
browser.find_element_by_id('answer').send_keys(ans)
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
browser.find_element_by_css_selector('[type="submit"]').click()


browser.close()