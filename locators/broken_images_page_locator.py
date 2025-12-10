from selenium.webdriver.common.by import By

class BrokenImagesPageLocators:
    AD_BANNER_LOCATOR = (By.XPATH, "//img[@alt='Fork me on GitHub']")
    BROKEN_IMAGES_1 = (By.XPATH, '//div[@class="example"]//img[@src][1]')
    BROKEN_IMAGES_2 = (By.XPATH, '//div[@class="example"]//img[@src][2]')
    BROKEN_IMAGES_LIST = [BROKEN_IMAGES_1, BROKEN_IMAGES_2]
    IMAGE = (By.XPATH, '//img[@src="img/avatar-blank.jpg"]')
