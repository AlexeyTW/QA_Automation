from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com'
    BASKET_BUTTON = (By.XPATH, "//a[text()='View basket']")


class LoginPageLocators:
    LOGIN_SUBSTRING = '/accounts/login'
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')
    FIELD_EMAIL = (By.ID, 'id_registration-email')
    FIELD_PASSWORD = (By.ID, 'id_registration-password1')
    FIELD_PASSWORD_REPEATED = (By.ID, 'id_registration-password2')
    BUTTON_REGISTER = (By.CSS_SELECTOR, 'button[name*="registration"]')


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
    ANY_PRODUCT_IN_THE_BASKET = (By.XPATH, "//h2[text()='Items to buy now']")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


