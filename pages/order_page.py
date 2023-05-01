import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ввести данные в поле ввода с плейсхолдером Имя")
    def set_name_one(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[0].send_keys("Кирилл")

    @allure.step("Ввести данные в поле ввода с плейсхолдером Имя")
    def set_name_two(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[0].send_keys("Кирилл")

    @allure.step("Ввести данные в поле ввода с плейсхолдером Фамилия")
    def set_surname_one(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[1].send_keys("Тищенко")

    @allure.step("Ввести данные в поле ввода с плейсхолдером Фамилия")
    def set_surname_two(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[1].send_keys("Тищенко")

    @allure.step(
        "Ввести данные в поле ввода с плейсхолдером Адрес: куда привести заказ"
    )
    def set_address(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[2].send_keys(
            "Москва, Зорге, 36"
        )

    @allure.step("Ввести данные в поле ввода с плейсхолдером Станция метро")
    def set_metro_station(self):
        self.driver.find_element(*OrderPageLocators.metro_station_input).send_keys(
            "Выхино"
        )
        self.driver.find_element(*OrderPageLocators.metro_station).click()

    @allure.step(
        "Ввести данные в поле ввода с плейсхолдером Телефон: на него позвонит курьер"
    )
    def set_phone_number(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[3].send_keys(
            "+79850600206"
        )

    @allure.step("Нажать кнопку Далее")
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()

    @allure.step("Ввести данные в поле ввода с плейсхолдером Когда привезти самокат")
    def set_date(self):
        self.driver.find_elements(*OrderPageLocators.second_page)[0].send_keys(
            "01.05.2023"
        )
        self.driver.find_element(*OrderPageLocators.date).click()

    @allure.step("Выбрать срок аренды из выпадающего списка Срок аренды")
    def set_rental_period_seven_days(self):
        self.driver.find_element(*OrderPageLocators.dropdown_control).click()
        self.driver.find_elements(*OrderPageLocators.dropdown_option)[6].click()

    @allure.step("Выбрать цвет самоката чёрный жемчуг")
    def click_black_checkbox(self):
        self.driver.find_element(*OrderPageLocators.black_checkbox).click()

    @allure.step("Выбрать цвет самоката серая безысходность")
    def click_grey_checkbox(self):
        self.driver.find_element(*OrderPageLocators.grey_checkbox).click()

    @allure.step("Ввести данные в поле ввода с плейсхолдером Комментарий для курьера")
    def set_comment_one(self):
        self.driver.find_elements(*OrderPageLocators.second_page)[1].send_keys("")

    @allure.step("Ввести данные в поле ввода с плейсхолдером Комментарий для курьера")
    def set_comment_two(self):
        self.driver.find_elements(*OrderPageLocators.second_page)[1].send_keys("")

    @allure.step("Нажать кнопку Заказать")
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    @allure.step("Нажать кнопку Да")
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    @allure.step("Получить текст Заказ оформлен")
    def order_has_been_placed_text(self):
        return (
            WebDriverWait(self.driver, 5)
            .until(ec.visibility_of_element_located(OrderPageLocators.text))
            .text
        )
