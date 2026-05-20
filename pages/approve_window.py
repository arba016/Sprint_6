import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.approve_order_page import ApproveOrderPageLocators



class ApproveWindow:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть на кнопку 'Да' в окне подтверждения заказа")
    def click_yes_button(self, browser_wait):
        browser_wait.until(
            EC.element_to_be_clickable(ApproveOrderPageLocators.YES_BUTTON)
        ).click()