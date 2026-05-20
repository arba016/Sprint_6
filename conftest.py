import pytest

from data import BASE_URL
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():

    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(BASE_URL)

    yield browser

    browser.quit()


@pytest.fixture
def browser_wait(driver):
    return WebDriverWait(driver, 5)