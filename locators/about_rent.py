from selenium.webdriver.common.by import By


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
    