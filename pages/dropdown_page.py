from pages.base_page import BasePage
from locators.dropdown_page_locators import DropdownPageLocators
dropdown_page_locators = DropdownPageLocators()


class DropdownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)