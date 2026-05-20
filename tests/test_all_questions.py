import allure
import pytest

from data import (
    ANSWER_TEXT_ONE,
    ANSWER_TEXT_TWO,
    ANSWER_TEXT_THREE,
    ANSWER_TEXT_FOUR,
    ANSWER_TEXT_FIVE,
    ANSWER_TEXT_SIX,
    ANSWER_TEXT_SEVEN,
    ANSWER_TEXT_EIGHT,
)
from locators.questions import QuestionsLocators, AnswerLocators
from pages.all_questions_section import QuestionsAndAnswers


@allure.title("Проверка всех вопросов и ответов на странице")
@allure.description("Проверяем, что при клике на каждый вопрос открывается правильный ответ.")
class TestAllQuestions:

    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_text",
        [
            (QuestionsLocators.FIRST_QUESTION, AnswerLocators.FIRST_ANSWER, ANSWER_TEXT_ONE),
            (QuestionsLocators.SECOND_QUESTION, AnswerLocators.SECOND_ANSWER, ANSWER_TEXT_TWO),
            (QuestionsLocators.THIRD_QUESTION, AnswerLocators.THIRD_ANSWER, ANSWER_TEXT_THREE),
            (QuestionsLocators.FOURTH_QUESTION, AnswerLocators.FOURTH_ANSWER, ANSWER_TEXT_FOUR),
            (QuestionsLocators.FIFTH_QUESTION, AnswerLocators.FIFTH_ANSWER, ANSWER_TEXT_FIVE),
            (QuestionsLocators.SIXTH_QUESTION, AnswerLocators.SIXTH_ANSWER, ANSWER_TEXT_SIX),
            (QuestionsLocators.SEVENTH_QUESTION, AnswerLocators.SEVENTH_ANSWER, ANSWER_TEXT_SEVEN),
            (QuestionsLocators.EIGHTH_QUESTION, AnswerLocators.EIGHTH_ANSWER, ANSWER_TEXT_EIGHT),
        ],
    )
    def test_question_answer(self, driver, browser_wait, question_locator, answer_locator, expected_text):
        questions_page = QuestionsAndAnswers(driver)

        questions_page.open_question(browser_wait, question_locator)
        actual_text = questions_page.get_answer_text(browser_wait, answer_locator)

        assert actual_text == expected_text, f"Текст ответа не совпадает с ожидаемым. Ожидалось: '{expected_text}', но получено: '{actual_text}'"