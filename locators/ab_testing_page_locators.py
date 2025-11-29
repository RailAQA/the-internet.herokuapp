from selenium.webdriver.common.by import By

class AbTestingPageLocators:
    TITLE_AB_TESTING_PAGE_LOCATOR = (By.XPATH, '//div[@id="content"]//div//h3')
    DESCRIPTION_AB_TETSTING_PAGE_LOCATOR = (By.XPATH, '//div[@id="content"]//div//p')