from pages.base_page import BasePage
from locators.challenging_dom_page_locators import ChallengingDomPageLocators
home_page_locators = ChallengingDomPageLocators()



class ChallengingDomPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)