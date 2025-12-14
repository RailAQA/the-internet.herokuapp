from selenium.webdriver.common.by import By

class DragAndDropPageLocators:
    BOX_1 = (By.ID, 'column-a')
    BOX_2 = (By.ID, 'column-b')
    BOX_1_TITTLE = (By.XPATH, '//div[@id="column-a"]//header')
    BOX_2_TITTLE = (By.XPATH, '//div[@id="column-b"]//header')