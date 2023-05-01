from selenium.webdriver.common.by import By


class MainPageLocators:
    locator_ya_logo = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    locator_samokat_logo = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    locator_order_button = [By.CLASS_NAME, "Button_Button__ra12g"]
    locator_cookie_button = [By.ID, "rcc-confirm-button"]

    locator_question_one_element = [By.ID, "accordion__heading-0"]
    locator_question_two_element = [By.ID, "accordion__heading-1"]
    locator_question_three_element = [By.ID, "accordion__heading-2"]
    locator_question_four_element = [By.ID, "accordion__heading-3"]
    locator_question_five_element = [By.ID, "accordion__heading-4"]
    locator_question_six_element = [By.ID, "accordion__heading-5"]
    locator_question_seven_element = [By.ID, "accordion__heading-6"]
    locator_question_eight_element = [By.ID, "accordion__heading-7"]

    locator_answer_one_element = [[By.ID, "accordion__panel-0"]]
    locator_answer_two_element = [By.ID, "accordion__panel-1"]
    locator_answer_three_element = [By.ID, "accordion__panel-2"]
    locator_answer_four_element = [By.ID, "accordion__panel-3"]
    locator_answer_five_element = [By.ID, "accordion__panel-4"]
    locator_answer_six_element = [By.ID, "accordion__panel-5"]
    locator_answer_seven_element = [By.ID, "accordion__panel-6"]
    locator_answer_eight_element = [By.ID, "accordion__panel-7"]
