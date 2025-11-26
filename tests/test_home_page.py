from pages.home_page import HomePage
from urls.links import URL
import pytest
import allure



@allure.epic('HomePage')
class TestHomePage:
    
    @allure.suite('Смоук тесты HomePage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_home_page
    class TestSmokeHomePage:
        """
        Общие смоук тесты для страницы HomePage
        """

        @allure.title('Проверка открытия главной страницы')
        @allure.description('Главная страница должна открываться и полностью загружаться')
        def test_is_home_page_opened(self, driver):
            home_page = HomePage(driver)
            home_page.open(URL.HOME_PAGE)
            assert home_page.is_page_loaded(URL.HOME_PAGE)
    
    class TestRegressHomePage:
        pass
