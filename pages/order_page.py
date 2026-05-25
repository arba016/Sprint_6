import allure

from pages.base_page import BasePage
from datetime import datetime, timedelta
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Проверяем, что открылось окно заказа")
    def check_order_window(self):
        self.wait_visibility(OrderPageLocators.ORDER_TITLE)

    @allure.step("Вводим имя {name}")
    def input_name(self, name):
        self.send_text(OrderPageLocators.NAME_INPUT, name)
    
    @allure.step("Вводим фамилию {surname}")
    def input_surname(self, surname):
        self.send_text(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step("Вводим адрес {adress}")
    def input_adress(self, adress):
        self.send_text(OrderPageLocators.ADDRESS_INPUT, adress)

    @allure.step("Кликнуть по выпадающему списку метро")
    def click_metro_button(self):
        self.click_element(OrderPageLocators.METRO_INPUT)

    @allure.step("Проверяем, что открылся выпадающий список со станциями метро")
    def check_metro_stations(self):
        self.wait_clickable(OrderPageLocators.METRO_STATION)

    @allure.step("Выбираем станцию метро ")
    def click_set_metro(self):
        self.click_element(OrderPageLocators.METRO_STATION)

    @allure.step("Вводим номер телефона {tel_number}")
    def input_phone_number(self, tel_number):
        self.send_text(OrderPageLocators.NUMBER_INPUT, tel_number)

    @allure.step("Кликнуть на кнопку 'Далее'")
    def click_next_button(self):
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @staticmethod
    def get_tomorrow_date():
        tomorrow = datetime.now() + timedelta(days=1)
        return tomorrow.strftime("%d.%m.%Y")
    
    @allure.step("Выбираем дату аренды")
    def date_rent(self):
        tomorrow_date = self.get_tomorrow_date()

        with allure.step(f"Выбираем дату аренды {tomorrow_date}"):
            self.click_element(OrderPageLocators.DATE_INPUT)
            self.send_text(OrderPageLocators.DATE_INPUT, tomorrow_date)
            self.click_by_esc(OrderPageLocators.DATE_INPUT)
            self.wait_invisibility(OrderPageLocators.CALENDAR)

    @allure.step("Нажимаем на поле выбора срока аренды")
    def click_rental_perriod_button(self):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_BUTTON)

    @allure.step("Выбираем период аренды 'три дня'")
    def rent_period(self):
        self.click_element(OrderPageLocators.THREE_DAYS)

    @allure.step("Выбираем цвет самоката: {color}")
    def choose_scooter_color(self, color):
        colors = {
            "grey": OrderPageLocators.GRAY_COLOR,
            "black": OrderPageLocators.BLACK_COLOR,
        }

        self.click_element(colors[color])

    @allure.step("Вводим комментарий для курьера {comment}")
    def comment_for_courier(self, comment):
        self.send_text(OrderPageLocators.COMMENT, comment)

    @allure.step("Кликнуть на кнопку 'Заказать' в окне 'Про аренду' ")
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Кликнуть на кнопку 'Да' в окне подтверждения заказа")
    def click_yes_button(self):
        self.click_element(OrderPageLocators.YES_BUTTON)

    @allure.step("Проверяем, что открылось окно с информацией о заказе")
    def check_window_complete_order(self):
        self.wait_visibility(OrderPageLocators.STATUS_ORDER_TEXT)

    @allure.step("Получаем текст окна успешного заказа")
    def get_complete_order_text(self):
        return self.wait_visibility(OrderPageLocators.STATUS_ORDER_TEXT).text

    @allure.description("Заполняем форму заказа самоката")
    def order_scooter(self, name, surname, address, tel_number, comment, color):
        self.check_order_window()
        self.input_name(name)
        self.input_surname(surname)
        self.input_adress(address)
        self.click_metro_button()
        self.click_set_metro()
        self.input_phone_number(tel_number)
        self.click_next_button()
        self.date_rent()
        self.click_rental_perriod_button()
        self.rent_period()
        self.choose_scooter_color(color)
        self.comment_for_courier(comment)
        self.click_order_button()
        self.click_yes_button()
        self.check_window_complete_order()