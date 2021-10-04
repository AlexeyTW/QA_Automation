from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_SUBSTRING = '/accounts/login'
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[class*='add-to-basket']")
