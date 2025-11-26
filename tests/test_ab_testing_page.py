import pytest
from urls.links import URL
from pages.ab_testing_page import AbTestingPage
import allure




@allure.epic('AbTestingPage')
class TestAbTestingPage:
    
    @allure.suite('Смоук тесты AbTestingPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_ab_testing_page
    class TestSmokeAbTestingPage:
        """
        Общие смоук тесты для страницы AbTestingPage
        """

        @allure.title('Проверка открытия страницы A/B Testing')
        @allure.description('Страница A/B Testing должна открываться и полностью загружаться')
        def test_is_ab_testing_page_opened(self, driver):
            a_b_testing = AbTestingPage(driver)
            a_b_testing.open(URL.A_B_TESTING_PAGE)
            assert a_b_testing.is_page_loaded(URL.A_B_TESTING_PAGE)