from .base_page import BasePage
from .locators import ProductPageLocators, PromoPagesLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import math

class ProductPage(BasePage):

    def go_to_product_page(self):
        product_link = self.browser.find_element(*ProductPageLocators.PRODUCT_LINK)
        product_link.click()

    def get_product_name(self, product_name):
        return self.browser.find_element(*product_name).text

    def get_product_price(self, product_price):
        return self.browser.find_element(*product_price).text

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def solve_alert_task(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code is {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('You must have the second alert present')

    def get_name_of_added_item(self, added_item):
        return self.browser.find_element(*added_item).text

    def get_price_of_basket(self, basket_price):
        return self.browser.find_element(*basket_price).text