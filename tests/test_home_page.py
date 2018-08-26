import pytest
from browser.browser import Browser
from pages.home_page import HomePage


@pytest.fixture
def browser():
    browser = Browser()
    yield browser
    browser.quit()


def test_hamburger_menu(browser):
    browser.navigate('https://utest.90min.com/')
    home_page = HomePage(browser)
    home_page.click_on_hamburger()
    assert home_page.validate_menu_open()


def test_fixtures_icon(browser):
    browser.navigate('https://utest.90min.com/')
    home_page = HomePage(browser)
    home_page.click_on_fixtures_icon()
    assert 'scores' in browser.get_url()
