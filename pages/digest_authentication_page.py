from pages.base_page import BasePage
from locators.digest_authentication_page_locators import DigestAuthenticationPageLocators
ab_testing_page_locators = DigestAuthenticationPageLocators()


class DigestAuthenticationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)