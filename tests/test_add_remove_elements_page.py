import pytest
from urls.links import URL
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