from pages.base_page import BasePage
from locators.broken_images_page_locator import BrokenImagesPageLocators
home_page_locators = BrokenImagesPageLocators()



class BrokenImagesPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)