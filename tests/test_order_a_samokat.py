import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.description("Кнопка «Заказать» вверху страницы")
    @allure.title("сценарий заказа самоката -- кнопка «Заказать» вверху страницы")
    def test_order_one(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        main_page.click_first_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_one()
        order_page.set_surname_one()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button()
        order_page.set_date()
        order_page.set_rental_period_seven_days()
        order_page.click_grey_checkbox()
        order_page.set_comment_one()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith("Заказ оформлен")

    @allure.description("Кнопка «Заказать» внизу страницы")
    @allure.title("сценарий заказа самоката -- кнопка «Заказать» внизу страницы")
    def test_order_two(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        main_page.click_second_order_button()
        order_page = OrderPage(driver)
        order_page.set_name_two()
        order_page.set_surname_two()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button()
        order_page.set_date()
        order_page.set_rental_period_seven_days()
        order_page.click_black_checkbox()
        order_page.set_comment_two()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith("Заказ оформлен")
