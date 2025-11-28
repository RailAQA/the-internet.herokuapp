from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePageLocators():
    TOTAL_LINKS_LOCATOR = (By.XPATH, "//li//a")
    AB_TESTING_LINK_LOCATOR = (By.XPATH, "//a[text()='A/B Testing']")
    ADD_REMOVE_ELEMENTS_LINK_LOCATOR = (By.XPATH, "//a[text()='Add/Remove Elements']")
    BASIC_AUTH_LINK_LOCATOR = (By.XPATH, "//a[text()='Basic Auth']")
    BROKEN_IMAGES_LINK_LOCATOR = (By.XPATH, "//a[text()='Broken Images']")
    CHALLENGING_DOM_LINK_LOCATOR = (By.XPATH, "//a[text()='Challenging DOM']")
    CHECKBOXES_LINK_LOCATOR = (By.XPATH, "//a[text()='Checkboxes']")
