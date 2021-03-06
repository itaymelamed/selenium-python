from selenium import webdriver
from browser_helper.browser_helper import BrowserHelper


class Browser:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.browser_helper = BrowserHelper(self.driver)

    def navigate(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def maximize(self):
        self.driver.maximize_window()

    def get_url(self):
        return self.driver.current_url
