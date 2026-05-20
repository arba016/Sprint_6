import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page import OrderPageLocators


class OrderScooterPage: 
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверяем, что открылось окно заказа")
    def check_order_window(self, browser_wait):
        browser_wait.until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_TITLE)
        )

    @allure.step("Вводим имя {name}")
    def input_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys(name)

    @allure.step("Вводим фамилию {surname}")
    def input_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)

    @allure.step("Вводим адрес {adress}")
    def input_adress(self, adress):

        self.driver.find_element(*OrderPageLocators.ADRESS_INPUT).send_keys(adress)

    @allure.step("Кликнуть по выпадающему списку метро")
    def click_metro_button(self):
        self.driver.find_element(*OrderPageLocators.METRO_INPUT).click()

    @allure.step("Проверяем, что открылся выпадающий список со станциями метро")
    def check_metro_stations(self, browser_wait):
        browser_wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_STATION))

    @allure.step("Выбираем станцию метро ")
    def click_set_metro(self):
        self.driver.find_element(*OrderPageLocators.METRO_STATION).click()

    @allure.step("Вводим номер телефона {tel_number}")
    def input_phone_number(self, tel_number):
        self.driver.find_element(*OrderPageLocators.NUMBER_INPUT).send_keys(tel_number)

    @allure.step("Кликнуть на кнопку 'Далее'")
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    @allure.description("Заполняем форму заказа самоката")
    def order_scooter(self, name, surname, adress, tel_number):
        self.input_name(name)
        self.input_surname(surname)
        self.input_adress(adress)
        self.click_metro_button()
        self.click_set_metro()
        self.input_phone_number(tel_number)
        self.click_next_button()