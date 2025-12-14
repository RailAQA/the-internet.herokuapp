import pytest
from config.links import URL
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

    @allure.suite('Регресс тесты DragAndDropPage')
    @pytest.mark.regression
    @pytest.mark.regression_drag_and_drop_page
    class TestRegressDragAndDropPage:
        """
        Регрессионные тесты для страницы DragAndDropPage
        """
        
        @pytest.mark.regression_module_drag_and_drop_age
        @allure.severity(allure.severity_level.CRITICAL)
        @allure.feature('Модуль Buttons в DragAndDropPage')
        class TestRegressionBoxesModule:
            """
            Регресс тесты на модуль Boxes.
            """

            @allure.title('Проверка по умолчанию тайтлы Box_1 = "A" и Box_2 = "B"')
            def test_boxes_tittles(self, driver):
                drag_and_drop_page = DragAndDropPage(driver)
                drag_and_drop_page.open(URL.DRAG_AND_DROP)
                actual_box_1_text = drag_and_drop_page.get_box_1_text()
                actual_box_2_text = drag_and_drop_page.get_box_2_text()
                expected_box_1_text = 'A'
                expected_box_2_text = 'B'
                assert actual_box_1_text == expected_box_1_text
                assert actual_box_2_text == expected_box_2_text

            @allure.title('Проверка перетаскивания боксаА на БоксБ')
            def test_drag_and_drop_boxes(self, driver):
                drag_and_drop_page = DragAndDropPage(driver)
                drag_and_drop_page.open(URL.DRAG_AND_DROP)
                drag_and_drop_page.drag_and_drop_boxes()
                actual_box_1_text = drag_and_drop_page.get_box_1_text()
                expected_box_1_text = 'B'
                assert actual_box_1_text == expected_box_1_text

            @allure.title('Проверка перетаскивание на любое свободное место')
            def test_drag_and_drop_boxes_to_empty_space(self, driver):
                drag_and_drop_page = DragAndDropPage(driver)
                drag_and_drop_page.open(URL.DRAG_AND_DROP)
                drag_and_drop_page.drag_and_drop_by_offset_boxes()
                actual_box_1_text = drag_and_drop_page.get_box_1_text()
                expected_box_1_text = 'A'
                assert actual_box_1_text == expected_box_1_text