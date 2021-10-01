from selenium.webdriver import Chrome

class BasePage:
    def __init__(self, browser: Chrome, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
