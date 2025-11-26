from selenium.webdriver.common.by import By

class HomePageLocators:
    AD_BANNER_LOCATOR = (By.XPATH, "//img[@alt='Fork me on GitHub']")
    AB_TESTING_LINK = (By.XPATH, "//a[text()='A/B Testing']")
