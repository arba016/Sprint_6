from selenium.webdriver.common.by import By


class MainPageLocators:
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_SECOND_BUTTON = (
        By.CSS_SELECTOR,
        ".Button_Button__ra12g.Button_UltraBig__UU3Lp",
    )
    SCOOTER_IMAGE = (By.CSS_SELECTOR, 'img[src="/assets/scooter.png"]')
    TEXT_SCOOTER = (By.CLASS_NAME, "Home_Header__iJKdX")