import allure
import pytest

from data import BASE_URL, ORDER_DATA
from pages.order_scooter_page import OrderScooterPage
from pages.approve_window import ApproveWindow
from pages.info_order_window import InfoOrderWindow
from pages.about_rent import AboutRent
from pages.main_page import MainPage


@allure.parent_suite("UI-тесты")
@allure.suite("Заказ самоката")
@allure.feature("Проверка заказа самоката")
class TestOrderScooter:

    @allure.title("Заказ самоката")
    @allure.description("Проверяем полный позитивный сценарий заказа самоката с разными данными и разными точками входа.")
    @pytest.mark.parametrize(
        "button_type, name, surname, address, phone, comment, color",
        ORDER_DATA,
    )
    def test_order_scooter(self, driver, browser_wait, button_type, name, surname, address, phone, comment, color):
        driver.get(BASE_URL)

        main_page = MainPage(driver)

        if button_type == "top":
            main_page.click_order_first_button()
        elif button_type == "bottom":
            main_page.scroll_to_second_order_button()
            main_page.click_to_second_order_button()

        order_page = OrderScooterPage(driver)
        order_page.check_order_window(browser_wait)
        order_page.order_scooter(name, surname, address, phone)

        about_rent = AboutRent(driver)
        about_rent.complete_order(browser_wait, comment, color)

        approve = ApproveWindow(driver)
        approve.click_yes_button(browser_wait)

        info_order_window = InfoOrderWindow(driver)
        actual_text = info_order_window.get_complete_order_text(browser_wait)

        assert "Заказ оформлен" in actual_text, (
            f"Ожидали, что в окне будет текст 'Заказ оформлен', "
            f"но получили: '{actual_text}'"
        )