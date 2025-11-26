from pages.base_page import BasePage
from locators.add_remove_elements_page_locators import AddRemoveElementsPageLocators
ab_testing_page_locators = AddRemoveElementsPageLocators()


class AddRemoveElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)