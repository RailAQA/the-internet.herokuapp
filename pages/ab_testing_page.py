from pages.base_page import BasePage
from locators.ab_testing_page_locators import AbTestingPageLocators
from data.data import DataTextABTestingPage
ab_testing_page_locators = AbTestingPageLocators()


class AbTestingPage(BasePage):
    def get_expected_title(self):
        return DataTextABTestingPage.title
    
    def get_current_title(self):
        return self.find(ab_testing_page_locators.TITLE_AB_TESTING_PAGE_LOCATOR).text
    
    def get_expected_description(self):
        return DataTextABTestingPage.description
    
    def get_current_description(self):
        return self.find(ab_testing_page_locators.DESCRIPTION_AB_TETSTING_PAGE_LOCATOR).text