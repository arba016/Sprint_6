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

class OrderPageAboutRentLocators:
    DATE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_BUTTON = (By.CLASS_NAME, "Dropdown-control")
    DAY = (By.XPATH, '//div[text()= "сутки"]')
    TWO_DAYS = (By.XPATH, '//div[text()= "двое суток"]')
    THREE_DAYS = (By.XPATH, '//div[text()= "трое суток"]')
    FOUR_DAYS = (By.XPATH, '//div[text()= "четверо суток"]')
    FIVE_DAYS = (By.XPATH, '//div[text()= "пятеро суток"]')
    SIX_DAYS = (By.XPATH, '//div[text()= "шестеро суток"]')
    SEVEN_DAYS = (By.XPATH, '//div[text()= "семеро суток"]')
    BLACK_COLOR = (By.ID, "black")
    GRAY_COLOR = (By.ID, "grey")
    COMMENT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, '//button[text()="Назад"]')
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']",
    )

class ApproveOrderPageLocators:
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    NO_BUTTON = (By.XPATH, "//button[text()='Нет']")

class StatusOrderWindow:
    STATUS_ORDER_TEXT = (By.XPATH,
    "//div[contains(@class, 'Order_Modal') and contains(., 'Заказ оформлен')]")
