from pages.base_page import BasePage
from locators.ab_testing_page_locators import AbTestingPageLocators
ab_testing_page_locators = AbTestingPageLocators()


class AbTestingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)