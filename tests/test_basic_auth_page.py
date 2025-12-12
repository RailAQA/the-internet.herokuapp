import pytest
from config.links import URL
from pages.basic_auth_page import BasicAuthPage
import allure
from time import sleep


@allure.epic('BasicAuthPage')
class TestBasicAuthPage:
    
    @allure.suite('Смоук тесты BasicAuthPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_basic_auth_page
    class TestSmokeBasicAuthPage:
        """
        Общие смоук тесты для страницы BasicAuthPage
        """

        @allure.title('Проверка открытия страницы BasicAuthPage')
        @allure.description('Cтраница BasicAuthPage должна открываться и полностью загружаться')
        def test_is_basic_auth_page_opened(self, driver):
            basic_auth_page = BasicAuthPage(driver)
            basic_auth_page.open(URL.BASIC_AUTH)
            assert basic_auth_page.is_page_loaded(URL.BASIC_AUTH)

    @allure.suite('Регресс тесты BasicAuthPage')
    @pytest.mark.regression
    @pytest.mark.regression_basic_auth_page
    class TestRegressBasicAuthPage:
        """
        Регрессионные тесты для страницы BasicAuthPage
        """
        
        @pytest.mark.regression_module_basic_auth_page
        @allure.severity(allure.severity_level.CRITICAL)
        @allure.feature('Модуль auth в BasicAuthPage')
        class TestRegressionAuthModule:
            """
            Регресс тесты на модуль авторизации. Для Firefox скипп
            """

            @allure.title('Проверка авторизации невалидным паролем')
            @allure.description('Авторизация невалидным паролем не проходит')
            def test_auth_with_invalid_password(self, driver):   
                basic_auth_page = BasicAuthPage(driver)
                basic_auth_page.open(URL.BASIC_AUTH)
                basic_auth_page.auth_with_invalid_password()
                assert basic_auth_page.auth_congralutations_page_is_not_loaded()

            @allure.title('Проверка авторизации невалидным логином')
            @allure.description('Авторизация невалидным логином не проходит')
            def test_auth_with_invalid_login(self, driver):   
                basic_auth_page = BasicAuthPage(driver)
                basic_auth_page.open(URL.BASIC_AUTH)
                basic_auth_page.auth_with_invalid_login()
                assert basic_auth_page.auth_congralutations_page_is_not_loaded()

            @allure.title('Проверка авторизации с пустым логином')
            @allure.description('Авторизация с пустым логином не проходит')
            def test_auth_with_empty_login(self, driver):   
                basic_auth_page = BasicAuthPage(driver)
                basic_auth_page.open(URL.BASIC_AUTH)
                basic_auth_page.auth_with_empty_login()
                assert basic_auth_page.auth_congralutations_page_is_not_loaded()

            @allure.title('Проверка авторизации с пустым паролем')
            @allure.description('Авторизация с пустым паролем не проходит')
            def test_auth_with_empty_password(self, driver):   
                basic_auth_page = BasicAuthPage(driver)
                basic_auth_page.open(URL.BASIC_AUTH)
                basic_auth_page.auth_with_empty_password()
                assert basic_auth_page.auth_congralutations_page_is_not_loaded()

            @allure.title('Проверка авторизации с пустым паролем и пустым логином')
            @allure.description('Авторизация с пустым паролем и логином не проходит')
            def test_auth_with_empty_password(self, driver):   
                basic_auth_page = BasicAuthPage(driver)
                basic_auth_page.open(URL.BASIC_AUTH)
                basic_auth_page.auth_with_empty_inputs()
                assert basic_auth_page.auth_congralutations_page_is_not_loaded()

        @pytest.mark.regression_test_button_module_congralutations_basic_auth_page
        @allure.severity(allure.severity_level.MINOR)
        @allure.feature('Модуль text в BasicAuthPage')
        class TestRegressionCongralutationsAuthModule:

            @allure.title('Проверка h1 заголовка на странице BasicAuthPage')
            @allure.description('Заголовок = Basic Auth')
            def test_title_congrat_module(self, driver):
                basic_auth_page = BasicAuthPage(driver)
                basic_auth_page.open(URL.BASIC_AUTH)
                basic_auth_page.auth_with_valid_log_and_pass()
                actual_title = basic_auth_page.get_actual_title()
                expected_title = basic_auth_page.get_expected_tittle()
                assert actual_title == expected_title

            @allure.title('Проверка описания на странице BasicAuthPage')
            @allure.description('Текст = Congratulations! You must have the proper credentials.')
            def test_decription_congrat_module(self, driver):
                basic_auth_page = BasicAuthPage(driver)
                basic_auth_page.open(URL.BASIC_AUTH)
                basic_auth_page.auth_with_valid_log_and_pass()
                actual_descrtiption = basic_auth_page.get_actual_description()
                expected_descrtiption = basic_auth_page.get_expected_description()
                assert actual_descrtiption == expected_descrtiption