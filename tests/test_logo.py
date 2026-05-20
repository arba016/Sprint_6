import allure

from data import BASE_URL, DZEN_URL
from pages.main_page import MainPage


@allure.parent_suite("UI-тесты")
@allure.suite("Главная страница")
@allure.feature("Проверка логотипов")
class TestLogo:

    @allure.title("Клик по логотипу Яндекса открывает страницу Яндекса/Дзена")
    @allure.description("Проверяем, что после клика по логотипу Яндекса открывается новая вкладка со страницей Дзена.")
    def test_click_yandex_logo_opens_yandex_page(self, driver, browser_wait):
        main_page = MainPage(driver)

        main_page.click_logo_yandex()
        main_page.switch_to_new_tab(browser_wait)
        main_page.check_url_after_click(browser_wait, DZEN_URL)

        assert DZEN_URL in main_page.get_current_url(), (
            f"Ожидали, что URL содержит '{DZEN_URL}', "
            f"но получили '{main_page.get_current_url()}'"
        )

    @allure.title("Клик по логотипу Самоката открывает главную страницу")
    @allure.description("Проверяем, что после клика по логотипу Самоката открывается главная страница Самоката.")
    def test_click_scooter_logo_opens_main_page(self, driver, browser_wait):
        main_page = MainPage(driver)

        main_page.scroll_to_second_order_button()
        main_page.click_to_second_order_button()
        main_page.click_logo_scooter()
        main_page.check_scooter_main_page_url(browser_wait, BASE_URL)

        assert main_page.get_current_url() == BASE_URL, (
            f"Ожидали URL '{BASE_URL}', "
            f"но получили '{main_page.get_current_url()}'"
        )