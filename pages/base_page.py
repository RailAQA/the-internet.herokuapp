from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.logging import *
from config.settings import settings
from selenium.common.exceptions import (NoSuchElementException, NoAlertPresentException, TimeoutException)
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
        return self.driver.find_element(*args)

    @allure.step('Поиск элементов по локатору')
    def finds(self, args):
        """
        Поиск элемента по локатору {args}
        :param args: Локатор элементов
        """
        return self.driver.find_elements(*args)

    def current_url(self):
        return self.driver.current_url

    @allure.step('Клик по элементу')
    def click_to(self, args):
        """
        Клик по элементу с локатором {*args}
        :param args: Локатор элемента, на который кликаем
        """
        try:
            self.driver.find_element(args).click()
        except NoSuchElementException:
            logger.error(f'элемент с локатором {args} не кликабельный')
            raise AssertionError(f'элемент с локатором {args} не кликабельный')
        
    @allure.step('Клик по элементам')
    def clicks_to(self, args):
        """
        Клик по элементу с локатором {*args}
        :param args: Локатор элемента, на который кликаем
        """
        try:
            elements = self.finds(args)
            for i in range(len(elements)):
                elements[i].click()
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
        
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
            logger.info('Аллерт есть на странице')
            return True
        except NoAlertPresentException:
            #ogger.critical('Аллерт не найден')
            return False
            

    @allure.step('Переключиться на алерт')
    @property
    def switch_to_alert_and(self):
        alert = self.driver.switch_to.alert
        return alert
    
    @allure.step('Передать значение в инпут аллерта')
    def send_text_to_input_in_alert(self, value: str):
        #self.switch_to_alert_and.send_keys(value)
        self.driver.switch_to.alert.send_keys(value)

    @allure.step('Переключиться на следующий инпут в аллерте')
    def switch_to_next_input_in_alert(self):
        self.send_text_to_input_in_alert(Keys.TAB)

    @allure.step('Подтвердить аллерт')
    def alert_accept(self):
        self.switch_to_alert_and.accept()

    @allure.step('Скиппнуть аллерт')
    def alert_close(self):
        self.driver.switch_to.alert.dismiss()