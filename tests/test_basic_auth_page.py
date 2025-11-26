import pytest
from config.links import URL
from pages.basic_auth_page import BasicAuthPage
import allure



@allure.epic('BasicAuthPage')
class TestBasicAuthPage:
    
    @allure.suite('Смоук тесты BasicAuthPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_basic_auth_page
    class TestSmokeBasicAuthPage:
        """
        Общие смоук тесты для страницы BasicAuthPage
        """

        @allure.title('Проверка открытия страницы BasicAuthPage')
        @allure.description('Cтраница BasicAuthPage должна открываться и полностью загружаться')
        def test_is_basic_auth_page_opened(self, driver):
            basic_auth_page = BasicAuthPage(driver)
            basic_auth_page.open(URL.BASIC_AUTH)
            assert basic_auth_page.is_page_loaded(URL.BASIC_AUTH)