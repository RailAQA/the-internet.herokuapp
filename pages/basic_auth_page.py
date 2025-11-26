from pages.base_page import BasePage
from locators.basic_auth_page_locators import BasicAuthPageLocators
home_page_locators = BasicAuthPageLocators()

class BasicAuthPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)