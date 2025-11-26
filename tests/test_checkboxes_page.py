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