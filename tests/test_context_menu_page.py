import pytest
from config.links import URL
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

    @allure.suite('Регресс тесты ContextMenuPage')
    @pytest.mark.regression
    @pytest.mark.regression_context_menu_page
    class TestRegressContextMenuPage:
        """
        Регрессионные тесты для страницы ContextMenuPage
        """
        
        @pytest.mark.regression_module_context_manu_page
        @allure.severity(allure.severity_level.CRITICAL)
        @allure.feature('Модуль BOX в ContextMenuPage')
        class TestRegressionBoxModule:
            """
            Регресс тесты на модуль BOX.
            """

            @allure.title('Проверка появляется алерт по правому клику на бокс')
            def test_alert_after_right_click(self, driver):
                context_menu_page = ContextMenuPage(driver)
                context_menu_page.open(URL.CONTEXT_MENU)
                context_menu_page.right_click_on_box()
                assert context_menu_page.is_alert_present()

            @allure.title('Проверка не появляется алерт по правому клику на любое пустое место')
            def test_right_click_on_empty_space(self, driver):
                context_menu_page = ContextMenuPage(driver)
                context_menu_page.open(URL.CONTEXT_MENU)
                context_menu_page.right_click_on_empty_space()
                assert not context_menu_page.is_alert_present()

            @allure.title('Проверка не появляется алерт по левому клику на бокс')
            def test_right_click_on_box(self, driver):
                context_menu_page = ContextMenuPage(driver)
                context_menu_page.open(URL.CONTEXT_MENU)
                context_menu_page.left_click_on_box()
                assert not context_menu_page.is_alert_present()