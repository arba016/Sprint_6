import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class QuestionsAndAnswers:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем вопрос")
    def open_question(self, browser_wait, question_locator):
        question = browser_wait.until(
            EC.visibility_of_element_located(question_locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            question
        )
        question = browser_wait.until(
            EC.element_to_be_clickable(question_locator)
        )
        question.send_keys(Keys.ENTER)

    @allure.step("Получаем текст ответа")
    def get_answer_text(self, browser_wait, answer_locator):
        answer = browser_wait.until(
            EC.visibility_of_element_located(answer_locator)
        )
        return answer.text