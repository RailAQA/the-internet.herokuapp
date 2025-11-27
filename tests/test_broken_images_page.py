import pytest
from config.links import URL
from pages.broken_images_page import BrokenImagesPage
import allure



@allure.epic('BrokenImagesPage')
class TestBrokenImagesPage:
    
    @allure.suite('Смоук тесты BrokenImagesPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_broken_images_page
    class TestSmokeBrokenImagesPage:
        """
        Общие смоук тесты для страницы BrokenImagesPage
        """

        @allure.title('Проверка открытия страницы BrokenImagesPage')
        @allure.description('Cтраница BrokenImagesPage должна открываться и полностью загружаться')
        def test_is_broken_images_page_opened(self, driver):
            broken_images_page = BrokenImagesPage(driver)
            broken_images_page.open(URL.BROKEN_IMAGES)
            assert broken_images_page.is_page_loaded(URL.BROKEN_IMAGES)