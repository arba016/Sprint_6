import allure
import pytest

from data import ORDER_DATA
from pages.order_page import OrderPage
from pages.main_page import MainPage

class TestOrderScooter:

    @allure.title("Заказ самоката через верхнюю кнопку 'Заказать'")
    @allure.description("Проверяем позитивный сценарий заказа через верхнюю кнопку.")
    @pytest.mark.parametrize(
        "name, surname, address, phone, comment",
        ORDER_DATA,
    )
    def test_order_scooter_from_top_button(
        self, driver, name, surname, address, phone, comment
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_top_order_button()
        order_page.order_scooter(name, surname, address, phone, comment, color='black')
        actual_text = order_page.get_complete_order_text()

        assert "Заказ оформлен" in actual_text, (
            f"Ожидали, что в окне будет текст 'Заказ оформлен', "
            f"но получили: '{actual_text}'"
        )

    @allure.title("Заказ самоката через нижнюю кнопку 'Заказать'")
    @allure.description("Проверяем позитивный сценарий заказа через нижнюю кнопку.")
    @pytest.mark.parametrize(
        "name, surname, address, phone, comment",
        ORDER_DATA,
    )
    def test_order_scooter_from_bottom_button(
        self, driver, name, surname, address, phone, comment
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_bottom_order_button()
        order_page.order_scooter(name, surname, address, phone, comment, color ='grey')
        actual_text = order_page.get_complete_order_text()

        assert "Заказ оформлен" in actual_text, (
            f"Ожидали, что в окне будет текст 'Заказ оформлен', "
            f"но получили: '{actual_text}'"
        )