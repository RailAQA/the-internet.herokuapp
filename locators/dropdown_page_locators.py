from selenium.webdriver.common.by import By

class DropdownPageLocators:
    DROPDOWN = (By.XPATH, '//select')
    DROPDOWN_VALUE_1 = (By.XPATH, '//option[@value="1"]')
    DROPDOWN_VALUE_2 = (By.XPATH, '//option[@value="2"]')