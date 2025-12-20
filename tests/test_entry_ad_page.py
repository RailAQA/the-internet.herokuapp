import pytest
from config.links import URL
from pages.entry_ad_page import EntryAdPage
from locators.entry_ad_page_locators import EntryAdPageLocators
import allure



@allure.epic('EntryAdPage')
class TestEntryAdPage:
    
    @allure.suite('Смоук тесты EntryAdPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_entry_ad_page
    class TestSmokeEntryAdPage:
        """
        Общие смоук тесты для страницы EntryAdPage
        """

        @allure.title('Проверка открытия страницы EntryAdPage')
        @allure.description('Страница EntryAdPage должна открываться и полностью загружаться')
        def test_is_entry_ad_opened(self, driver):
            entry_ad_page = EntryAdPage(driver)
            entry_ad_page.open(URL.ENTRY_AD)
            assert entry_ad_page.is_page_loaded(URL.ENTRY_AD)

    @allure.suite('Регресс тесты EntryAdPage')
    @pytest.mark.regression
    @pytest.mark.regression_entry_ad_page
    class TestRegressEntryAdPage:
        """
        Регрессионные тесты для страницы EntryAdPage
        """
        
        @pytest.mark.regression_module_modal_window
        @allure.severity(allure.severity_level.CRITICAL)
        @allure.feature('Модуль Modal Window в EntryAdPage')
        class TestRegressionModalModalWindowModule:
            """
            Регресс тесты на модуль Modal Window.
            """

            @allure.title('Проверка модальное окно отображается при заходе на страницу')
            def test_modal_window(self, driver):
                entry_ad_page = EntryAdPage(driver)
                entry_ad_page.open(URL.ENTRY_AD)
                modal_window = entry_ad_page.wait_element_will_visible(5, EntryAdPageLocators().MODAL_WINDOW)
                assert modal_window.is_displayed()

            @allure.title('Проверка модальное окно отображается после обновления страницы')
            def test_modal_window_after_reloading_page(self, driver):
                entry_ad_page = EntryAdPage(driver)
                entry_ad_page.open(URL.ENTRY_AD)
                entry_ad_page.refresh_page()
                modal_window = entry_ad_page.wait_element_will_visible(5, EntryAdPageLocators().MODAL_WINDOW)
                assert modal_window.is_displayed()
