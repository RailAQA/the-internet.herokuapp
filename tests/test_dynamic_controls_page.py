import pytest
from urls.links import URL
from pages.dynamic_controls_page import DynamicControlsPage
import allure



@allure.epic('DynamicControlsPage')
class TestDynamicControlsPage:
    
    @allure.suite('Смоук тесты DynamicControlsPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_dynamic_controls_page
    class TestSmokeDynamicControlsPage:
        """
        Общие смоук тесты для страницы DynamicControlsPage
        """

        @allure.title('Проверка открытия страницы DynamicControlsPage')
        @allure.description('Cтраница DynamicControlsPage должна открываться и полностью загружаться')
        def test_is_dynamic_content_page_opened(self, driver):
            dynamic_controls_page = DynamicControlsPage(driver)
            dynamic_controls_page.open(URL.DYNAMIC_CONTROLS)
            assert dynamic_controls_page.is_page_loaded(URL.DYNAMIC_CONTROLS)