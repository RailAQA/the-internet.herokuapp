import pytest
from urls.links import URL
from pages.entry_ad_page import EntryAdPage
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