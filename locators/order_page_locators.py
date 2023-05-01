from selenium.webdriver.common.by import By


class OrderPageLocators:
    inputs = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    metro_station_input = [
        By.XPATH,
        "//input[contains(@placeholder, '* Станция метро')]",
    ]
    metro_station = [By.XPATH, '//li[@class = "select-search__row"][1]']
    next_button = [By.XPATH, "//button[contains(text(), 'Далее')]"]
    second_page = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    date = [By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]"]
    dropdown_control = [By.CLASS_NAME, "Dropdown-control"]
    dropdown_option = [By.CLASS_NAME, "Dropdown-option"]
    black_checkbox = [By.ID, "black"]
    grey_checkbox = [By.ID, "grey"]
    order_button = [
        By.XPATH,
        "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle__1CSJM')]",
    ]
    yes_button = [
        By.XPATH,
        "//button[contains(text(), 'Да') and contains(@class, 'Button_Middle__1CSJM')]",
    ]
    text = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
