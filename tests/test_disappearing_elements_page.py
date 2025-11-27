import pytest
from config.links import URL
from pages.disappearing_elements_page import DisappearingElementsPage
import allure



@allure.epic('DisappearingElementsPage')
class TestDisappearingElementsPage:
    
    @allure.suite('Смоук тесты DisappearingElementsPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_disappearing_elements_page
    class TestSmokeDisappearingElementsPage:
        """
        Общие смоук тесты для страницы DisappearingElementsPage
        """

        @allure.title('Проверка открытия страницы DisappearingElementsPage')
        @allure.description('Cтраница DisappearingElementsPage должна открываться и полностью загружаться')
        def test_is_disappearing_elements_page_opened(self, driver):
            disappearing_elements_page = DisappearingElementsPage(driver)
            disappearing_elements_page.open(URL.DISAPPEARING_ELEMENTS)
            assert disappearing_elements_page.is_page_loaded(URL.DISAPPEARING_ELEMENTS)