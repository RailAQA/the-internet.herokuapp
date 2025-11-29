from selenium.webdriver.common.by import By


class AddRemoveElementsPageLocators:
    ADD_ELEMENTS_BUTTON_LOCATOR = (By.XPATH, '//button[@onclick="addElement()"]')
    DELETE_BUTTON_LOCATOR = (By.XPATH, '//div[@id="elements"]//button')