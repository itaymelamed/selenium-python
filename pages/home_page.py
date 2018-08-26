from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.hamburger_btn = lambda: self.driver.find_element(By.CSS_SELECTOR, '.main-sidenav-toggle')
        self.hamburger_menu = lambda: self.driver.find_element(By.CSS_SELECTOR, '.main-sidenav')
        self.fixtures_icon = lambda: self.driver.find_element(By.CSS_SELECTOR, '.nm-icon-fixtures_icon')

    def click_on_hamburger(self):
        self.browser_helper.wait_for_element(self.hamburger_btn)
        self.hamburger_btn().click()

    def validate_menu_open(self):
        return self.browser_helper.wait_for_element(self.hamburger_menu)

    def click_on_fixtures_icon(self):
        self.browser_helper.wait_for_element(self.fixtures_icon)
        self.fixtures_icon().click()
