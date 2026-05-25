import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def browser_wait(self):
        return WebDriverWait(self.driver, 5)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_visibility(self, locator):
        return self.browser_wait().until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator):
        return self.browser_wait().until(
            EC.element_to_be_clickable(locator)
        )

    def wait_invisibility(self, locator):
        return self.browser_wait().until(
            EC.invisibility_of_element_located(locator)
        )

    def click_element(self, locator):
        self.wait_clickable(locator).click()

    def send_text(self, locator, text):
        self.wait_visibility(locator).send_keys(text)

    def scroll_to_element(self, locator):
        element = self.wait_visibility(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def scroll_and_click(self, locator):
        element = self.wait_visibility(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        self.driver.execute_script("arguments[0].click();", element)

    def wait_url_contains(self, expected_url):
        return self.browser_wait().until(
            EC.url_contains(expected_url)
        )

    def wait_url_to_be(self, expected_url):
        return self.browser_wait().until(
            EC.url_to_be(expected_url)
        )

    def switch_to_new_tab(self):
        self.browser_wait().until(
            lambda driver: len(driver.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        return self.wait_visibility(locator).text
    
    def open_page(self, url):
        self.driver.get(url)

    def is_url_contains(self, expected_url):
        try:
            self.browser_wait().until(
                EC.url_contains(expected_url)
            )
            return True
        except TimeoutException:
            return False
        
    def press_key(self, locator, key):
        self.wait_visibility(locator).send_keys(key)

    def click_by_enter(self, locator):
        self.wait_clickable(locator).send_keys(Keys.ENTER)

    def click_by_esc(self, locator):
        self.wait_clickable(locator).send_keys(Keys.ESCAPE)