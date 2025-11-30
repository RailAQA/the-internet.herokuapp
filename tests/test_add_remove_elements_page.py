import pytest
from config.links import URL
from pages.add_remove_elements_page import AddRemoveElementsPage
import allure




@allure.epic('AddRemoveElementsPage')
class TestAddRemoveElementsPage:
    
    @allure.suite('Смоук тесты AddRemoveElementsPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_add_remove_elements_page
    class TestAddRemoveElementsPage:
        """
        Общие смоук тесты для страницы AddRemoveElements
        """

        @allure.title('Проверка открытия страницы AddRemoveElements')
        @allure.description('Страница AddRemoveElements должна открываться и полностью загружаться')
        def test_is_add_remove_elements_page_opened(self, driver):
            add_remove_elements_page = AddRemoveElementsPage(driver)
            add_remove_elements_page.open(URL.ADD_REMOVE_ELEMENTS)
            assert add_remove_elements_page.is_page_loaded(URL.ADD_REMOVE_ELEMENTS)

    @allure.suite('Регресс тесты AddRemoveElementsPage')
    @pytest.mark.regression
    @pytest.mark.regression_add_remove_elements_page
    class TestRegressAddRemoveElementsPage:
        """
        Регрессионные тесты для страницы AddRemoveElementsPage
        """
        
        @pytest.mark.regression_test_button_module_add_remove_elements_page
        @allure.severity(allure.severity_level.CRITICAL)
        @allure.feature('Модуль text в AddRemoveElementsPage')
        class TestRegressionButtonsModule:
            


            @allure.title('Проверка по нажатию на ADD добавляется 1 кнопка Delete button')
            @allure.description('Примечание: в тесте используется рандомное число кликов')
            def test_add_elements(self, driver):
                add_remove_elements_page = AddRemoveElementsPage(driver)
                add_remove_elements_page.open(URL.ADD_REMOVE_ELEMENTS)
                add_remove_elements_page.click_add_button()
                count_clicks_to_add_buttons = add_remove_elements_page.count_added_delete_buttons()
                actual_count_delete_buttons = add_remove_elements_page.actual_count_delete_buttons()
                assert count_clicks_to_add_buttons == actual_count_delete_buttons

            def test_delete_elements(self, driver):
                add_remove_elements_page = AddRemoveElementsPage(driver)
                add_remove_elements_page.open(URL.ADD_REMOVE_ELEMENTS)
                add_remove_elements_page.click_add_button()
                add_remove_elements_page.click_to_delete_button()
                count_clicks_to_add_buttons = add_remove_elements_page.count_added_delete_buttons()
                count_click_to_delete_button = add_remove_elements_page.count_deleted_delete_buttons()
                actual_count_delete_buttons = add_remove_elements_page.actual_count_delete_buttons()
                assert actual_count_delete_buttons == count_clicks_to_add_buttons - count_click_to_delete_button

            def test_delete_all_buttons(self, driver):
                add_remove_elements_page = AddRemoveElementsPage(driver)
                add_remove_elements_page.open(URL.ADD_REMOVE_ELEMENTS)
                add_remove_elements_page.click_add_button()
                add_remove_elements_page.delete_all_added_buttons()
                count_actual_buttons = add_remove_elements_page.actual_count_delete_after_deletion()
                assert count_actual_buttons == 0