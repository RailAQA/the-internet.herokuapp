import pytest
from config.links import URL
from pages.dropdown_page import DropdownPage
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