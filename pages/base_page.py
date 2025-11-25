from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, TimeoutException)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """
        Открытие страницы {url}
        """
        return self.driver.get(url)
        
    def find(self, args):
        """
        Поиск элемента по локатору {args}
        """
        self.driver.find_element(*args)

    def click_to(self, args):
        """
        Клик по элементу с локатором {*args}
        """
        try:
            self.click_to(args)
            self.driver.find_element(*args).click()
        except NoSuchElementException:
            raise AssertionError(f'элемент с локатором {args} не найден')
        
    def scroll_to(self, args):
        self.driver.execute_script("return arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", args)

    def wait_element_will_visible(self, timeout: int, args):
        """
        Явное ожидание пока элемент с локатором {args} станет видимым в течение {timeout}
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(args))
        except TimeoutError:
            raise AssertionError(f'элемент с локатором {args} не появился в течение {timeout}')
        except TimeoutException:
            raise AssertionError(f'элемент с локатором {args} не появился в течение {timeout}')
        
    def wait_element_will_invisible(self, timeout: int, args):
        """
        Явное ожидание пока элемент с локатором {args} станет невидимым в течение {timeout}
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(args))
        except TimeoutError:
            raise AssertionError(f'элемент с локатором {args} не исчез в течение {timeout}')
        except TimeoutException:
            raise AssertionError(f'элемент с локатором {args} не исчез в течение {timeout}')
        
    def wait_element_will_clickable(self, timeout: int, args):
        """
        Явное ожидание пока элемент с локатором {args} станет кликабельным в течение {timeout}
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(args))
        except TimeoutError:
            raise AssertionError(f'элемент с локатором {args} не стал кликабельным в течение {timeout}')
        except TimeoutException:
            raise AssertionError(f'элемент с локатором {args} не стал кликабельным в течение {timeout}')
        
    def wait_element_will_not_clickable(self, timeout: int, args):
        """
        Явное ожидание пока элемент с локатором {args} станет НЕкликабельным в течение {timeout}
        """
        try:
            return WebDriverWait(self.driver, timeout).until_not(EC.element_to_be_clickable(args))
        except TimeoutError:
            raise AssertionError(f'элемент с локатором {args} не стал HEкликабельным в течение {timeout}')
        except TimeoutException:
            raise AssertionError(f'элемент с локатором {args} не стал HEкликабельным в течение {timeout}')

