import pytest
from config.links import URL
from pages.disappearing_elements_page import DisappearingElementsPage
from locators.disappearing_elements_page_locators import DisappearingElementsLocators
import allure



@allure.epic('DisappearingElementsPage')
class TestDisappearingElementsPage:
    
    @allure.suite('Смоук тесты DisappearingElementsPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_disappearing_elements_page
    class TestSmokeDisappearingElementsPage:
        """
        Общие смоук тесты для страницы DisappearingElementsPage
        """

        @allure.title('Проверка открытия страницы DisappearingElementsPage')
        @allure.description('Cтраница DisappearingElementsPage должна открываться и полностью загружаться')
        def test_is_disappearing_elements_page_opened(self, driver):
            disappearing_elements_page = DisappearingElementsPage(driver)
            disappearing_elements_page.open(URL.DISAPPEARING_ELEMENTS)
            assert disappearing_elements_page.is_page_loaded(URL.DISAPPEARING_ELEMENTS)

    @allure.suite('Регресс тесты DisappearingElementsPage')
    @pytest.mark.regression
    @pytest.mark.regression_disappearing_elements_page
    class TestRegressDisappearingElementsPagePage:
        """
        Регрессионные тесты для страницы DisappearingElementsPage
        """
        
        @pytest.mark.regression_module_disappearing_elements_page
        @allure.severity(allure.severity_level.CRITICAL)
        @allure.feature('Модуль Buttons в DisappearingElementsPage')
        class TestRegressionButtonsModule:
            """
            Регресс тесты на модуль Buttons.
            """

            @allure.title('Проверка по умолчанию кнопка "Gallery" видимая')
            def test_gallery_button_visable(self, driver):
                disappearing_elements_page = DisappearingElementsPage(driver)
                disappearing_elements_page.open(URL.DISAPPEARING_ELEMENTS)
                gallery_button = disappearing_elements_page.find(DisappearingElementsLocators().GALLERY_BUTTON)
                assert gallery_button.is_displayed()

            @allure.title('Проверка кнопка "Gallery" пропадает после рефреша страницы')
            def test_gallery_button_disappearing(self, driver):
                disappearing_elements_page = DisappearingElementsPage(driver)
                disappearing_elements_page.open(URL.DISAPPEARING_ELEMENTS)
                disappearing_elements_page.refresh_page()
                gallery_button = disappearing_elements_page.find(DisappearingElementsLocators().GALLERY_BUTTON)
                assert not gallery_button.is_displayed(), f'Кнопка "Gallery" не пропала. Фактический результат: После рефреша страницы кнопка "Gallery" не стала невидимой'