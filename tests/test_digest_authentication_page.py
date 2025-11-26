import pytest
from urls.links import URL
from pages.digest_authentication_page import DigestAuthenticationPage
import allure



@allure.epic('DigestAuthenticationPage')
class TestDigestAuthenticationPage:
    
    @allure.suite('Смоук тесты DigestAuthenticationPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_digest_authentication_page
    class TestSmokeDigestAuthenticationPage:
        """
        Общие смоук тесты для страницы DigestAuthenticationPage
        """

        @allure.title('Проверка открытия страницы DigestAuthenticationPage')
        @allure.description('Cтраница DigestAuthenticationPage должна открываться и полностью загружаться')
        def test_is_digest_authentication_page_opened(self, driver):
            context_menu_page = DigestAuthenticationPage(driver)
            context_menu_page.open(URL.DIGEST_AUTHENTICATION)
            assert context_menu_page.is_page_loaded(URL.DIGEST_AUTHENTICATION)