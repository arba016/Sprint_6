import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_order_first_button(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON).click()

    @allure.step("Прокрутить до второй кнопки 'Заказать'")
    def scroll_to_second_order_button(self):
        second_order_button = self.driver.find_element(*MainPageLocators.ORDER_SECOND_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", second_order_button)

    @allure.step("Кликнуть на вторую кнопку 'Заказать'")
    def click_to_second_order_button(self):
        self.driver.find_element(*MainPageLocators.ORDER_SECOND_BUTTON).click()

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.YANDEX_LOGO).click()

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self, browser_wait):
        browser_wait.until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Проверяем, что открылась страница Дзена")
    def check_url_after_click(self, browser_wait, expected_url):
        browser_wait.until(EC.url_contains(expected_url))

    @allure.step("Кликнуть по логотипу Самоката")
    def click_logo_scooter(self):
        self.driver.find_element(*MainPageLocators.SCOOTER_LOGO).click()

    @allure.step("Проверям, что открылась главная страница Самоката")
    def check_text_main_page(self, browser_wait):
        browser_wait.until(EC.visibility_of_element_located(MainPageLocators.TEXT_SCOOTER))

    @allure.step("Проверяем, что открылась главная страница Самоката")
    def check_scooter_main_page_url(self, browser_wait, expected_url):
        browser_wait.until(EC.url_to_be(expected_url))

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверяем, что текст главной страницы отображается")
    def get_main_page_text(self, browser_wait):
        return browser_wait.until(
            EC.visibility_of_element_located(MainPageLocators.TEXT_SCOOTER)
        ).text