from .locators import BasePageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def check_basket_has_no_products(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY)

    def check_message_basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.ANY_PRODUCT_IN_THE_BASKET)