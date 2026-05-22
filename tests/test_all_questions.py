import allure
import pytest

from pages.main_page import MainPage
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
from locators.main_page_locators import QuestionsLocators, AnswerLocators

class TestAllQuestions:

    @allure.title("Проверка всех вопросов и ответов на странице")
    @allure.description("Проверяем, что при клике на каждый вопрос открывается правильный ответ.")
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
    def test_question_answer(self, driver, question_locator, answer_locator, expected_text):
        main_page = MainPage(driver)

        main_page.open_question(question_locator)
        actual_text = main_page.get_answer_text(answer_locator)

        assert actual_text == expected_text, (
            f"Ожидали текст ответа: '{expected_text}', "
            f"но получили: '{actual_text}'"
        )