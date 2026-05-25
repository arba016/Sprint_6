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
from locators.main_page_locators import MainPageLocators

class TestAllQuestions:

    @allure.title("Проверка всех вопросов и ответов на странице")
    @allure.description("Проверяем, что при клике на каждый вопрос открывается правильный ответ.")
    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_text",
        [
            (MainPageLocators.FIRST_QUESTION, MainPageLocators.FIRST_ANSWER, ANSWER_TEXT_ONE),
            (MainPageLocators.SECOND_QUESTION, MainPageLocators.SECOND_ANSWER, ANSWER_TEXT_TWO),
            (MainPageLocators.THIRD_QUESTION, MainPageLocators.THIRD_ANSWER, ANSWER_TEXT_THREE),
            (MainPageLocators.FOURTH_QUESTION, MainPageLocators.FOURTH_ANSWER, ANSWER_TEXT_FOUR),
            (MainPageLocators.FIFTH_QUESTION, MainPageLocators.FIFTH_ANSWER, ANSWER_TEXT_FIVE),
            (MainPageLocators.SIXTH_QUESTION, MainPageLocators.SIXTH_ANSWER, ANSWER_TEXT_SIX),
            (MainPageLocators.SEVENTH_QUESTION, MainPageLocators.SEVENTH_ANSWER, ANSWER_TEXT_SEVEN),
            (MainPageLocators.EIGHTH_QUESTION, MainPageLocators.EIGHTH_ANSWER, ANSWER_TEXT_EIGHT),
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