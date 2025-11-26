import pytest
from urls.links import URL
from pages.challenging_dom_page import ChallengingDomPage
import allure



@allure.epic('ChallengingDomPage')
class TestChallengingDomPage:
    
    @allure.suite('Смоук тесты ChallengingDomPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_challenging_dom_page
    class TestSmokeChallengingDomPage:
        """
        Общие смоук тесты для страницы ChallengingDomPage
        """

        @allure.title('Проверка открытия страницы ChallengingDomPage')
        @allure.description('Cтраница ChallengingDomPage должна открываться и полностью загружаться')
        def test_is_challenging_dom_page_opened(self, driver):
            challenging_dom_page = ChallengingDomPage(driver)
            challenging_dom_page.open(URL.CHALLENGING_DOM)
            assert challenging_dom_page.is_page_loaded(URL.CHALLENGING_DOM)