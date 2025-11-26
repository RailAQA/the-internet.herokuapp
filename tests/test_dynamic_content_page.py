import pytest
from config.links import URL
from pages.dynamic_content_page import DynamicContentPage
import allure



@allure.epic('DynamicContentPage')
class TestDynamicContentPage:
    
    @allure.suite('Смоук тесты DynamicContentPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_dynamic_content_page
    class TestSmokeDynamicContentPage:
        """
        Общие смоук тесты для страницы DynamicContentPage
        """

        @allure.title('Проверка открытия страницы DynamicContentPage')
        @allure.description('Cтраница DynamicContentPage должна открываться и полностью загружаться')
        def test_is_dynamic_content_page_opened(self, driver):
            dynamic_content_page = DynamicContentPage(driver)
            dynamic_content_page.open(URL.DYNAMIC_CONTENT)
            assert dynamic_content_page.is_page_loaded(URL.DYNAMIC_CONTENT)