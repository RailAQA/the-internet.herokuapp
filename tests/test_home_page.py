from pages.home_page import HomePage
from config.settings import settings
from config.links import URL
from locators.home_page_locators import HomePageLocators
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
            home_page.open(settings.BASE_URL)
            assert home_page.is_page_loaded(settings.BASE_URL)
    
    @allure.suite('Регресс тесты HomePage')
    @pytest.mark.regression
    @pytest.mark.regression_home_page
    class TestRegressHomePage:
        """
        Регрессионные тесты для страницы HomePage
        """
        @allure.severity(allure.severity_level.CRITICAL)
        class TestRegressionLinksModule:

            @allure.feature('Модуль links в HomePage')
            @pytest.mark.regression_links_home_page
            @allure.title('Проверка по клику на линк A/B Testing открывается страница с ссылкой /abtest')
            def test_click_to_ab_testing(self, driver):
                home_page = HomePage(driver)
                home_page.open(settings.BASE_URL)
                home_page.click_to_ab_testing_link()
                assert home_page.current_url() == URL.A_B_TESTING_PAGE
