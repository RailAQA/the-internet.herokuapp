import pytest
from urls.links import URL
from pages.context_menu_page import ContextMenuPage
import allure



@allure.epic('ContextMenuPage')
class TestContextMenuPage:
    
    @allure.suite('Смоук тесты ContextMenuPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_context_menu_page
    class TestSmokeContextMenuPage:
        """
        Общие смоук тесты для страницы ContextMenuPage
        """

        @allure.title('Проверка открытия страницы ContextMenuPage')
        @allure.description('Cтраница ContextMenuPage должна открываться и полностью загружаться')
        def test_is_context_menu_page_opened(self, driver):
            context_menu_page = ContextMenuPage(driver)
            context_menu_page.open(URL.CONTEXT_MENU)
            assert context_menu_page.is_page_loaded(URL.CONTEXT_MENU)