import pytest
from config.links import URL
from pages.broken_images_page import BrokenImagesPage
from locators.broken_images_page_locator import BrokenImagesPageLocators
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

        @allure.suite('Регресс тесты BrokenImagesPage')
        @pytest.mark.regression
        @pytest.mark.regression_broken_images_page
        class TestRegressBrokenImagePage:
            """
            Регрессионные тесты для страницы BrokenImagesPage
            """
            
            @pytest.mark.regression_module_broken_image_page
            @allure.severity(allure.severity_level.NORMAL)
            @allure.feature('Модуль image в BrokenImagesPage')
            class TestRegressionImageModule:
                """
                Регресс тесты на модуль image.
                """

                @pytest.mark.parametrize("broken_image", BrokenImagesPageLocators.BROKEN_IMAGES_LIST)
                def test_broken_image(self, driver, broken_image):
                    broken_images_page = BrokenImagesPage(driver)
                    broken_images_page.open(URL.BROKEN_IMAGES)
                    assert broken_images_page.image_is_broken(broken_image)
