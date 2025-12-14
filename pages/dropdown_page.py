from pages.base_page import BasePage
from locators.dropdown_page_locators import DropdownPageLocators
from generator.generator import generated_random_dropdown_value
from selenium.webdriver.support.ui import Select
dropdown_page_locators = DropdownPageLocators()


class DropdownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.random_value = generated_random_dropdown_value()
    
    def is_actual_value(self):
        element = self.find(dropdown_page_locators.DROPDOWN)
        return self.dropdown(element).first_selected_option.text
    
    def select_random_value(self):
        element = self.find(dropdown_page_locators.DROPDOWN)
        return self.dropdown(element).select_by_index(self.random_value)
    
    def get_selected_value(self):
        return "Option " + self.random_value