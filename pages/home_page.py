from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from config.settings import settings
home_page_locators = HomePageLocators()

class HomePage(BasePage):
    
    def click_to_ab_testing_link(self):
        self.click_to(HomePageLocators.AB_TESTING_LINK_LOCATOR)

    def click_to_add_remove_elements_link(self):
        self.click_to(HomePageLocators.ADD_REMOVE_ELEMENTS_LINK_LOCATOR)

    def click_to_basic_auth_link(self):
        self.click_to(HomePageLocators.BASIC_AUTH_LINK_LOCATOR)

    def click_to_broken_images_link(self):
        self.click_to(HomePageLocators.BROKEN_IMAGES_LINK_LOCATOR)

    def click_to_challenging_dom_link(self):
        self.click_to(HomePageLocators.CHALLENGING_DOM_LINK_LOCATOR)

    def click_to_checkboxes_link(self):
        self.click_to(HomePageLocators.CHECKBOXES_LINK_LOCATOR)   

    def list_of_all_links(self):
        return self.finds(HomePageLocators.TOTAL_LINKS_LOCATOR)
    
    def click_to_link_by_index(self, link_index, expected_url):
        """Кликает на ссылку по индексу"""
        links = self.list_of_all_links()
        if link_index < len(links):
            links[link_index].click()
        if 'auth' in expected_url:
            self.alert_close()
            self.open(expected_url.replace('http://', 'http://admin:admin@'))

        

        
    
    