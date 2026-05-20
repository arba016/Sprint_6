import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from locators.order_page import OrderPageLocators
from locators.about_rent import OrderPageAboutRentLocators



class AboutRent:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_tomorrow_date():
        tomorrow = datetime.now() + timedelta(days=1)
        return tomorrow.strftime("%d.%m.%Y")

    def date_rent(self, browser_wait):
        tomorrow_date = self.get_tomorrow_date()

        with allure.step(f"Выбираем дату аренды {tomorrow_date}"):
            date_input = browser_wait.until(
                EC.element_to_be_clickable(OrderPageAboutRentLocators.DATE_INPUT)
            )
            date_input.click()
            date_input.send_keys(self.get_tomorrow_date())
            date_input.send_keys(Keys.ESCAPE)
            browser_wait.until(
                EC.invisibility_of_element_located((OrderPageLocators.CALENDAR))
            )

    @allure.step("Выбираем период аренды 'три дня'")
    def rent_period(self, browser_wait):
        self.driver.find_element(
            *OrderPageAboutRentLocators.RENTAL_PERIOD_BUTTON
        ).click()

        browser_wait.until(
            EC.element_to_be_clickable(OrderPageAboutRentLocators.THREE_DAYS)
        ).click()

    @allure.step("Выбираем цвет самоката: {color}")
    def choose_scooter_color(self, color):
        if color == "grey":
            self.color_scooter_gray()
        elif color == "black":
            self.color_scooter_black()

    @allure.step("Выбираем серый цвет самоката")
    def color_scooter_gray(self):
        self.driver.find_element(*OrderPageAboutRentLocators.GRAY_COLOR).click()

    @allure.step("Выбираем черный цвет самоката")
    def color_scooter_black(self):
        self.driver.find_element(*OrderPageAboutRentLocators.BLACK_COLOR).click()

    @allure.step("Вводим комментарий для курьера {comment}")
    def comment_for_courier(self, comment):
        self.driver.find_element(*OrderPageAboutRentLocators.COMMENT).send_keys(comment)

    @allure.step("Кликнуть на кнопку 'Заказать' в окне 'Про аренду' ")
    def click_order_button(self):
        self.driver.find_element(*OrderPageAboutRentLocators.ORDER_BUTTON).click()

    @allure.step("Заполняем форму 'Про аренду' и кликаем на кнопку 'Заказать'")
    def complete_order(self, browser_wait, comment, color):
        self.date_rent(browser_wait)
        self.rent_period(browser_wait)
        self.choose_scooter_color(color)
        self.comment_for_courier(comment)
        self.click_order_button()