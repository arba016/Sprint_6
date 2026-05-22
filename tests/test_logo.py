import allure

from data import BASE_URL, DZEN_URL
from pages.main_page import MainPage

class TestLogo:

    @allure.title("Клик по логотипу Яндекса открывает страницу Яндекса/Дзена")
    @allure.description("Проверяем, что после клика по логотипу Яндекса открывается новая вкладка со страницей Дзена.")
    def test_click_yandex_logo_opens_yandex_page(self, driver):
        main_page = MainPage(driver)

        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        is_dzen_opened = main_page.is_url_contains(DZEN_URL)
        current_url = main_page.get_opened_page_url()

        assert is_dzen_opened, (
            f"Ожидали, что откроется страница '{DZEN_URL}', "
            f"но открылась '{current_url}'"
        )

    @allure.title("Клик по логотипу Самоката открывает главную страницу")
    @allure.description("Проверяем, что после клика по логотипу Самоката открывается главная страница Самоката.")
    def test_click_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.click_top_order_button()
        main_page.click_scooter_logo()
        main_page.wait_scooter_main_page_url(BASE_URL)
        current_url = main_page.get_opened_page_url()

        assert current_url == BASE_URL, (
            f"Ожидали URL '{BASE_URL}', "
            f"но получили '{current_url}'"
        )