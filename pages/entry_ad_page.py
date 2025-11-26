from pages.base_page import BasePage
from locators.entry_ad_page_locators import EntryAdPageLocators
entry_ad_page_locators = EntryAdPageLocators()


class EntryAdPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)