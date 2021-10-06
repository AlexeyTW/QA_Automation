from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_SUBSTRING = '/accounts/login'
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    PRODUCT_LINK = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page .row .product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[class*='add-to-basket']")
    PRODUCT_HAS_BEEN_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BASKET_PRICE = (By.XPATH, "//p[contains(text(), 'basket total')]/strong")

class PromoPagesLocators:
    PROMO_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

