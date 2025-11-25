from locators.home_page_locators import HomePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """
        Открытие страницы {url}
        """
        try:
            self.driver.get(url)
        except:
            pass

    def find(self, args):
        self.driver.find_element(*args)

    def click_to(self, args):
        self.driver.find_element(*args).click()

