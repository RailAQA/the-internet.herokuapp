import pytest
from config.links import URL
from pages.checkboxes_page import CheckboxesPage
import allure



@allure.epic('CheckboxesPage')
class TestCheckboxesPage:
    
    @allure.suite('Смоук тесты CheckboxesPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_checkboxes_page
    class TestSmokeCheckboxesPage:
        """
        Общие смоук тесты для страницы CheckboxesPage
        """

        @allure.title('Проверка открытия страницы CheckboxesPage')
        @allure.description('Cтраница CheckboxesPage должна открываться и полностью загружаться')
        def test_is_checkboxes_page_opened(self, driver):
            checkboxes_page = CheckboxesPage(driver)
            checkboxes_page.open(URL.CHECKBOXES)
            assert checkboxes_page.is_page_loaded(URL.CHECKBOXES)

    @allure.suite('Регресс тесты CheckBoxesPage')
    @pytest.mark.regression
    @pytest.mark.regression_checkboxes_page
    class TestRegressCheckBoxesPage:
        """
        Регрессионные тесты для страницы CheckBoxesPage
        """
        
        @pytest.mark.regression_module_checkbox_page
        @allure.severity(allure.severity_level.NORMAL)
        @allure.feature('Модуль чекбокс в CheckBoxesPage')
        class TestRegressionCheckboxModule:
            """
            Регресс тесты на модуль Чекбокс.
            """

            @allure.title('Проверка по умолчанию чекбоксы не активны')
            def test_checkboxes_actvity(self, driver):
                checkboxes_page = CheckboxesPage(driver)
                checkboxes_page.open(URL.CHECKBOXES)
                checkboxes_are_not_active = checkboxes_page.check_checkboxes_not_active()
                assert checkboxes_are_not_active, f'Один из чекбоксов активен по умолчанию'

            @allure.title('Проверка по клику на чекбокс становится активным')
            def test_checkbox_activation(self, driver):
                checkboxes_page = CheckboxesPage(driver)
                checkboxes_page.open(URL.CHECKBOXES)
                checkboxes_page.click_to_checkbox()
                checkbox_is_active = checkboxes_page.checkbox_is_active()
                assert checkbox_is_active, f'По клику на чекбокс не становится активным'

            @allure.title('Проверка по повторному клику на чекбокс становится НЕ активным')
            def test_checkbox_disable(self, driver):
                checkboxes_page = CheckboxesPage(driver)
                checkboxes_page.open(URL.CHECKBOXES)
                checkboxes_page.click_to_checkbox()
                checkboxes_page.disable_checkbox()
                checkbox_is_disabled = checkboxes_page.check_checkboxes_not_active()
                assert checkbox_is_disabled, f'По клику активный чекбокс не задизейблился'