from pages.base_page import BasePage
from locators.disappearing_elements_page_locators import DisappearingElementsLocators
disappearing_elements_locators = DisappearingElementsLocators()


class DisappearingElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)