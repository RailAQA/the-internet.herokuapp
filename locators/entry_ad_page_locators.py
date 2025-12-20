from selenium.webdriver.common.by import By

class EntryAdPageLocators:
    MODAL_WINDOW = (By.XPATH, '//div[@class="modal"]')
    MODAL_WINDOW_TEXT = (By.XPATH, '//div[@class="modal-body"]//p')
    CLOSE_BUTTON_IN_MODAL_WINDOW = (By.XPATH, '//div[@class="modal-footer"]')