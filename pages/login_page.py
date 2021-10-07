import pytest

from .locators import LoginPageLocators, BasePageLocators
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException



class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert EC.url_contains(LoginPageLocators.LOGIN_SUBSTRING)

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)

    def register_new_user(self, email, password):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        self.browser.find_element(*LoginPageLocators.FIELD_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD_REPEATED).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()
        assert not self.is_not_element_present(*BasePageLocators.USER_ICON), 'User icon is not present. Check registration'
        try:
            alert = self.browser.switch_to.alert
            alert.dismiss()
        except NoAlertPresentException:
            pass

