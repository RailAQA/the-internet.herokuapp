from pages.home_page import HomePage
from config.settings import settings
from config.links import URL
from locators.home_page_locators import HomePageLocators
from config.settings import settings
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
        @pytest.mark.regression_links_home_page
        @allure.severity(allure.severity_level.CRITICAL)
        @allure.feature('Модуль links в HomePage')
        class TestRegressionLinksModule:

            
            @pytest.mark.parametrize('link_index, expected_url', list(enumerate(URL.EXPECTED_URLS))[:15])
            def test_click_to_links_home_page(self, driver, link_index, expected_url):
                if 'auth' in expected_url and settings.BROWSER == 'firefox':
                    pytest.skip(f"Пропуск auth страницы в Firefox: {expected_url}")
                home_page = HomePage(driver)
                home_page.open(settings.BASE_URL)
                home_page.click_to_link_by_index(link_index, expected_url)  # ← передаем индекс
                assert home_page.current_url() == expected_url
