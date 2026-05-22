from selenium.webdriver.common.by import By


class MainPageLocators:
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BOTTOM_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']"
    )
    SCOOTER_IMAGE = (By.CSS_SELECTOR, 'img[src="/assets/scooter.png"]')
    TEXT_SCOOTER = (By.CLASS_NAME, "Home_Header__iJKdX")

class QuestionsLocators:
    FIRST_QUESTION = (By.ID, 'accordion__heading-0')
    SECOND_QUESTION = (By.ID, 'accordion__heading-1')
    THIRD_QUESTION = (By.ID, 'accordion__heading-2')
    FOURTH_QUESTION = (By.ID, 'accordion__heading-3')
    FIFTH_QUESTION = (By.ID, 'accordion__heading-4')
    SIXTH_QUESTION = (By.ID, 'accordion__heading-5')
    SEVENTH_QUESTION = (By.ID, 'accordion__heading-6')
    EIGHTH_QUESTION = (By.ID, 'accordion__heading-7')


class AnswerLocators:
    FIRST_ANSWER = (By.ID, 'accordion__panel-0')
    SECOND_ANSWER = (By.ID, 'accordion__panel-1')
    THIRD_ANSWER = (By.ID, 'accordion__panel-2')
    FOURTH_ANSWER = (By.ID, 'accordion__panel-3')
    FIFTH_ANSWER = (By.ID, 'accordion__panel-4')
    SIXTH_ANSWER = (By.ID, 'accordion__panel-5')
    SEVENTH_ANSWER = (By.ID, 'accordion__panel-6')
    EIGHTH_ANSWER = (By.ID, 'accordion__panel-7')