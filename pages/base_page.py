from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logging import *
from config.settings import settings
from selenium.common.exceptions import (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, TimeoutException)
import requests
import allure



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step(f'Запуск бразуера и открытие страницы')
    def open(self, url):
        """
        Открытие страницы {url}
        :param url: Проверяемая страница
        """
        return self.driver.get(url)
        
    @allure.step('Поиск элемента по локатору')
    def find(self, args):
        """
        Поиск элемента по локатору {args}
        :param args: Локатор искаемого элемента
        """
        self.driver.find_element(*args)

    def current_url(self):
        return self.driver.current_url

    @allure.step('Клик по элементу')
    def click_to(self, args):
        """
        Клик по элементу с локатором {*args}
        :param args: Локатор элемента, на который кликаем
        """
        try:
            self.driver.find_element(*args).click()
        except NoSuchElementException:
            logger.error(f'элемент с локатором {args} не кликабельный')
            raise AssertionError(f'элемент с локатором {args} не кликабельный')

    @allure.step('Скролл до нужного элемента на странице')  
    def scroll_to(self, args):
        """
        Сколл к элементу
        :param args: Локатор элемента, к которому скроллимся
        """
        self.driver.execute_script("return arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", args)

    @allure.step('Ожидание пока элемент станет видимым')
    def wait_element_will_visible(self, timeout: int, args):
        """
        Явное ожидание пока элемент с локатором {args} станет видимым в течение {timeout}
        :param timeout: Время ожидания
        :param args: Локатор элемента, который ожидаем
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(args))
        except TimeoutError:
            raise AssertionError(f'элемент с локатором {args} не появился в течение {timeout}')
        except TimeoutException:
            raise AssertionError(f'элемент с локатором {args} не появился в течение {timeout}')

    @allure.step('Ожидание пока элемент станет НЕвидимым')
    def wait_element_will_invisible(self, timeout: int, args):
        """
        Явное ожидание пока элемент с локатором {args} станет невидимым в течение {timeout}
        :param timeout: Время ожидания
        :param args: Локатор элемента, который ожидаем
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(args))
        except TimeoutError:
            raise AssertionError(f'элемент с локатором {args} не исчез в течение {timeout}')
        except TimeoutException:
            logger.error(f'элемент с локатором {args} не исчез в течение {timeout}')
            raise AssertionError(f'элемент с локатором {args} не исчез в течение {timeout}')

    @allure.step('Ожидание пока элемент станет кликабельным')
    def wait_element_will_clickable(self, timeout: int, args):
        """
        Явное ожидание пока элемент с локатором {args} станет кликабельным в течение {timeout}
        :param timeout: Время ожидания
        :param args: Локатор элемента, который ожидаем
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(args))
        except TimeoutError:
            logger.error(f'элемент с локатором {args} не стал кликабельным в течение {timeout}')
            raise AssertionError(f'элемент с локатором {args} не стал кликабельным в течение {timeout}')
        except TimeoutException:
            logger.error(f'элемент с локатором {args} не исчез в течение {timeout}')
            raise AssertionError(f'элемент с локатором {args} не стал кликабельным в течение {timeout}')

    @allure.step('Ожидание пока элемент станет НЕкликабельным')   
    def wait_element_will_not_clickable(self, timeout: int, args):
        """
        Явное ожидание пока элемент с локатором {args} станет НЕкликабельным в течение {timeout}
        :param timeout: Время ожидания
        :param args: Локатор элемента, который ожидаем
        """
        try:
            return WebDriverWait(self.driver, timeout).until_not(EC.element_to_be_clickable(args))
        except TimeoutError:
            logger.error(f'элемент с локатором {args} не стал HEкликабельным в течение {timeout}')
            raise AssertionError(f'элемент с локатором {args} не стал HEкликабельным в течение {timeout}')
        except TimeoutException:
            logger.error(f'элемент с локатором {args} не стал HEкликабельным в течение {timeout}')
            raise AssertionError(f'элемент с локатором {args} не стал HEкликабельным в течение {timeout}')
        
    @allure.step('Проверка открывается ли страница')
    def is_page_loaded(self, url, timeout=10):
        """
        для смоук тестов - открывается ли страница.
        :param url: Проверяемая страница
        :param timeout: Время за которое настроено ожидание
        """
        try:
            actual_status_code = requests.get(url)
            if 'auth' in url:
                if settings.BROWSER.lower() == 'chrome':
                    WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
                else:
                    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            else:
                WebDriverWait(self.driver, 10).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete")
            logger.info(f'Страница {url} успешно загружена')
            return True
        except TimeoutException:
            logger.critical(f'Страница {url} не загрузилась за {timeout} секунд. Фактический статус-код = {actual_status_code}')
            return False
