import allure
import pytest
from pages.main_page import MainPage


class TestMainPage:
    @allure.description(
        "Проверить: когда нажимаешь на стрелочку первого вопроса, открывается соответствующий текст ответа"
    )
    @pytest.mark.parametrize(
        "question_number, expected_answer",
        [
            (1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (8, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
        ],
    )
    def test_questions(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.click_question(question_number)
        answer = main_page.get_answer(question_number)
        assert answer == expected_answer
