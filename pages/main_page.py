import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Кликнуть на нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_and_click(MainPageLocators.ORDER_BOTTOM_BUTTON)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Кликнуть по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Проверить, что открылась главная страница Самоката")
    def wait_scooter_main_page_url(self, expected_url):
        self.wait_url_to_be(expected_url)

    @allure.step("Проверить, что открылась страница Дзена")
    def wait_dzen_url(self, expected_url):
        self.wait_url_contains(expected_url)

    @allure.step("Получить текст главной страницы")
    def get_main_page_text(self):
        return self.get_text(MainPageLocators.TEXT_SCOOTER)
    
    def get_opened_page_url(self):
        return self.get_current_url()
    
    @allure.step("Открыть вопрос")
    def open_question(self, question_locator):
        self.scroll_to_element(question_locator)
        self.click_by_enter(question_locator)

    @allure.step("Получить текст ответа")
    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)
    