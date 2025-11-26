from pages.base_page import BasePage
from locators.dynamic_controls_page_locators import DynamicControlsPageLocators
dynamic_controls_page_locators = DynamicControlsPageLocators()


class DynamicControlsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)