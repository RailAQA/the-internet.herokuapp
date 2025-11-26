import pytest
from urls.links import URL
from pages.drag_and_drop_page import DragAndDropPage
import allure



@allure.epic('DragAndDropPage')
class TestDragAndDropPage:
    
    @allure.suite('Смоук тесты DragAndDropPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_drag_and_drop_page
    class TestSmokeDragAndDropPage:
        """
        Общие смоук тесты для страницы DragAndDropPage
        """

        @allure.title('Проверка открытия страницы DragAndDropPage')
        @allure.description('Cтраница DragAndDropPage должна открываться и полностью загружаться')
        def test_is_drag_and_drop_page_opened(self, driver):
            drag_and_drop_page = DragAndDropPage(driver)
            drag_and_drop_page.open(URL.DRAG_AND_DROP)
            assert drag_and_drop_page.is_page_loaded(URL.DRAG_AND_DROP)