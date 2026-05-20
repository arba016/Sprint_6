from selenium.webdriver.common.by import By


class StatusOrderWindow:
    STATUS_ORDER_TEXT = By.XPATH,(
    "//div[contains(@class, 'Order_Modal') and contains(., 'Заказ оформлен')]")
