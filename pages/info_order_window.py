import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.status_order import StatusOrderWindow


class InfoOrderWindow:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверяем, что открылось окно с информацией о заказе")
    def check_window_complete_order(self, browser_wait):
        browser_wait.until(
            EC.visibility_of_element_located(StatusOrderWindow.STATUS_ORDER_TEXT)
        )

    @allure.step("Получаем текст окна успешного заказа")
    def get_complete_order_text(self, browser_wait):
        return browser_wait.until(
            EC.visibility_of_element_located(StatusOrderWindow.STATUS_ORDER_TEXT)
        ).text