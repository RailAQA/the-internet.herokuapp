from pages.base_page import BasePage
from locators.context_menu_page_locators import ContextMenuPageLocators
home_page_locators = ContextMenuPageLocators()



class ContextMenuPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)