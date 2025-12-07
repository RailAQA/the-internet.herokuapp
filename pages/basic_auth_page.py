from pages.base_page import BasePage
from locators.basic_auth_page_locators import BasicAuthPageLocators
from generator.generator import generated_auth_form
from config.settings import settings
from data.data import DataTextCongralutationsBasicAuthPage
from config.links import URL
from selenium.webdriver.common.keys import Keys
home_page_locators = BasicAuthPageLocators()

class BasicAuthPage(BasePage):
    
    def auth_with_valid_log_and_pass(self):
        random_auth_form = next(generated_auth_form())
        basic_auth_page = URL.BASIC_AUTH
        if 'http://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('http://', '')
        elif 'https://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('https://', '')
        auth_url = f"http://{settings.USER_LOGIN}:{settings.USER_PASSWORD}@{basic_auth_page}"
        self.open(auth_url)

    def auth_with_invalid_password(self):
        random_auth_form = next(generated_auth_form())
        basic_auth_page = URL.BASIC_AUTH
        if 'http://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('http://', '')
        elif 'https://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('https://', '')
        auth_url = f"http://{settings.USER_LOGIN}:{random_auth_form.password}@{basic_auth_page}"
        self.open(auth_url)

    def auth_with_invalid_login(self):
        random_auth_form = next(generated_auth_form())
        basic_auth_page = URL.BASIC_AUTH
        if 'http://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('http://', '')
        elif 'https://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('https://', '')
        auth_url = f"http://{random_auth_form.login}:{settings.USER_PASSWORD}@{basic_auth_page}"
        self.open(auth_url)

    def auth_with_empty_login(self):
        basic_auth_page = URL.BASIC_AUTH
        if 'http://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('http://', '')
        elif 'https://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('https://', '')
        auth_url = f"http://{settings.USER_EMPTY_LOGIN}:{settings.USER_PASSWORD}@{basic_auth_page}"
        self.open(auth_url)

    def auth_with_empty_password(self):
        basic_auth_page = URL.BASIC_AUTH
        if 'http://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('http://', '')
        elif 'https://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('https://', '')
        auth_url = f"http://{settings.USER_LOGIN}:{settings.USER_EMPTY_PASSWORD}@{basic_auth_page}"
        self.open(auth_url)

    def auth_with_empty_inputs(self):
        basic_auth_page = URL.BASIC_AUTH
        if 'http://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('http://', '')
        elif 'https://' in basic_auth_page:
            basic_auth_page = basic_auth_page.replace('https://', '')
        auth_url = f"http://{settings.USER_EMPTY_LOGIN}:{settings.USER_EMPTY_PASSWORD}@{basic_auth_page}"
        self.open(auth_url)

    def auth_congralutations_page_is_not_loaded(self):
        try:
            self.wait_element_will_invisible(5, BasicAuthPageLocators.TEXT_AUTH_CONGRALUTATIONS)
            return True
        except:
            return False
        
    def get_actual_title(self):
        return self.find(BasicAuthPageLocators.TITTLE_AUTH_CONGRALUTATIONS).text
    
    def get_expected_tittle(self):
        return DataTextCongralutationsBasicAuthPage().title
    
    def get_actual_description(self):
        return self.find(BasicAuthPageLocators.TEXT_AUTH_CONGRALUTATIONS).text
    
    def get_expected_description(self):
        return DataTextCongralutationsBasicAuthPage().description