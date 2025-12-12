from selenium.webdriver.common.by import By

class CheckboxesPageLocators:
    CHECKBOX_1 = (By.XPATH, '//form[@id="checkboxes"]//input[1]') # <- 1-й чекбокс
    CHECKBOX_2 = (By.XPATH, '//form[@id="checkboxes"]//input[2]') # <- 2-й чекбокс
    LIST_CHECKBOXES = (By.XPATH, '//form[@id="checkboxes"]//input')
    LIST_CHECKBOX = [CHECKBOX_1, CHECKBOX_2]