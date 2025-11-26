from pages.base_page import BasePage
from locators.dynamic_content_page_locators import DynamicContentPageLocators
dynamic_content_page_locators = DynamicContentPageLocators()


class DynamicContentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)