import allure
from pages.main_page import MainPage


class TestMainPage:
    @allure.description(
        "Проверить: когда нажимаешь на стрелочку первого вопроса, открывается соответствующий текст ответа"
    )
    @allure.title("когда нажимаешь на стрелочку, открывается соответствующий текст")
    def test_question_one(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page.click_question_one()
        assert (
            main_page.get_answer_one()
            == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        )

    @allure.description(
        "Проверить: когда нажимаешь на стрелочку второго вопроса, открывается соответствующий текст ответа"
    )
    @allure.title("когда нажимаешь на стрелочку, открывается соответствующий текст")
    def test_question_two(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)
        main_page.click_question_two()
        assert (
            main_page.get_answer_two()
            == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        )

    @allure.description(
        "Проверить: когда нажимаешь на стрелочку третьего вопроса, открывается соответствующий текст ответа"
    )
    @allure.title("когда нажимаешь на стрелочку, открывается соответствующий текст")
    def test_question_three(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)
        main_page.click_question_three()
        assert (
            main_page.get_answer_three()
            == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        )

    @allure.description(
        "Проверить: когда нажимаешь на стрелочку четвёртого вопроса, открывается соответствующий текст ответа"
    )
    @allure.title("когда нажимаешь на стрелочку, открывается соответствующий текст")
    def test_question_four(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)
        main_page.click_question_four()
        assert (
            main_page.get_answer_four()
            == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        )

    @allure.description(
        "Проверить: когда нажимаешь на стрелочку пятого вопроса, открывается соответствующий текст ответа"
    )
    @allure.title("когда нажимаешь на стрелочку, открывается соответствующий текст")
    def test_question_five(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)
        main_page.click_question_five()
        assert (
            main_page.get_answer_five()
            == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        )

    @allure.description(
        "Проверить: когда нажимаешь на стрелочку шестого вопроса, открывается соответствующий текст ответа"
    )
    @allure.title("когда нажимаешь на стрелочку, открывается соответствующий текст")
    def test_question_six(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)
        main_page.click_question_six()
        assert (
            main_page.get_answer_six()
            == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        )

    @allure.description(
        "Проверить: когда нажимаешь на стрелочку седьмого вопроса, открывается соответствующий текст ответа"
    )
    @allure.title("когда нажимаешь на стрелочку, открывается соответствующий текст")
    def test_question_seven(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)
        main_page.click_question_seven()
        assert (
            main_page.get_answer_seven()
            == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        )

    @allure.description(
        "Проверить: когда нажимаешь на стрелочку восьмого вопроса, открывается соответствующий текст ответа"
    )
    @allure.title("когда нажимаешь на стрелочку, открывается соответствующий текст")
    def test_question_eight(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)
        main_page.click_question_eight()
        assert (
            main_page.get_answer_eight()
            == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        )
