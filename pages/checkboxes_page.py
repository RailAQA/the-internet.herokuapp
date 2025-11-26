from pages.base_page import BasePage
from locators.checkboxes_page_locators import CheckboxesPageLocators
home_page_locators = CheckboxesPageLocators()



class CheckboxesPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)