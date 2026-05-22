import pytest

from data import BASE_URL
from selenium import webdriver



@pytest.fixture
def driver():

    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(BASE_URL)

    yield browser

    browser.quit()
    