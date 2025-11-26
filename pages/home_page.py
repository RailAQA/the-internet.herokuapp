from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
home_page_locators = HomePageLocators()

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_ab_testing_link(self):
        self.click_to(HomePageLocators.AB_TESTING_LINK)