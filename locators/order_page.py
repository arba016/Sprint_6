from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    SURNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADRESS_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Адрес: куда привезти заказ']",
    )
    METRO_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    METRO_STATION = (By.CSS_SELECTOR, "button[value = '2']")
    NUMBER_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Телефон: на него позвонит курьер']",
    )
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    ORDER_TITLE = (By.CLASS_NAME, "Order_Header__BZXOb")
    CALENDAR = (By.CLASS_NAME, "react-datepicker")
