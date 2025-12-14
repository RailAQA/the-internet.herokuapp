import pytest
from config.links import URL
from pages.dropdown_page import DropdownPage
from locators.dropdown_page_locators import DropdownPageLocators
import allure



@allure.epic('DropdownPage')
class TestDropdownPage:
    
    @allure.suite('Смоук тесты DropdownPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_drag_and_drop_page
    class TestSmokeDropdownPage:
        """
        Общие смоук тесты для страницы DropdownPage
        """

        @allure.title('Проверка открытия страницы DropdownPage')
        @allure.description('Cтраница DropdownPage должна открываться и полностью загружаться')
        def test_is_dropdown_page_opened(self, driver):
            dropdown_page = DropdownPage(driver)
            dropdown_page.open(URL.DROPDOWN)
            assert dropdown_page.is_page_loaded(URL.DROPDOWN)

    @allure.suite('Регресс тесты DropdownPage')
    @pytest.mark.regression
    @pytest.mark.regression_dropdown_page
    class TestRegressDropdownPage:
        """
        Регрессионные тесты для страницы DropdownPage
        """
        
        @pytest.mark.regression_module_dropdown_age
        @allure.severity(allure.severity_level.NORMAL)
        @allure.feature('Модуль Buttons в DropdownPage')
        class TestRegressionDropdownModule:
            """
            Регресс тесты на модуль Dropdown.
            """

            @allure.title('Проверка по умолчанию выбрано значение "Please select an option"')
            def test_default_dropdown_value(self, driver):
                dropdown_page = DropdownPage(driver)
                dropdown_page.open(URL.DROPDOWN)
                actual_selected_value = dropdown_page.is_actual_value()
                expected_selected_value = 'Please select an option'
                assert actual_selected_value == expected_selected_value

            @allure.title('Проверка выбора значения в dropdown')
            def test_dropdown_selecting(self, driver):
                dropdown_page = DropdownPage(driver)
                dropdown_page.open(URL.DROPDOWN)
                dropdown_page.select_random_value()
                selected_value = dropdown_page.get_selected_value()
                actual_value = dropdown_page.is_actual_value()
                assert selected_value == actual_value
