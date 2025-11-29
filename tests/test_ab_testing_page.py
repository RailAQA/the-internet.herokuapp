import pytest
from config.links import URL
from pages.ab_testing_page import AbTestingPage
import allure




@allure.epic('AbTestingPage')
class TestAbTestingPage:
    
    @allure.suite('Смоук тесты AbTestingPage')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.smoke_ab_testing_page
    class TestSmokeAbTestingPage:
        """
        Общие смоук тесты для страницы AbTestingPage
        """

        @allure.title('Проверка открытия страницы A/B Testing')
        @allure.description('Страница A/B Testing должна открываться и полностью загружаться')
        def test_is_ab_testing_page_opened(self, driver):
            a_b_testing = AbTestingPage(driver)
            a_b_testing.open(URL.A_B_TESTING_PAGE)
            assert a_b_testing.is_page_loaded(URL.A_B_TESTING_PAGE)

        @allure.suite('Регресс тесты AbTestingPage')
        @pytest.mark.regression
        @pytest.mark.regression_ab_testing_page
        class TestRegressAbTestingPage:
            """
            Регрессионные тесты для страницы AB_TESTING PAGE
            """
            @pytest.mark.regression_test_ab_testing_page
            @allure.severity(allure.severity_level.MINOR)
            @allure.feature('Модуль text в AbTestingPage')
            class TestRegressionTextModule:

                def test_ab_testing_page_title(self, driver):
                    a_b_testing = AbTestingPage(driver)
                    a_b_testing.open(URL.A_B_TESTING_PAGE)
                    expected_title = a_b_testing.get_expected_title()
                    actual_title = a_b_testing.get_current_title()
                    assert expected_title == actual_title, f'Заголовок страницы неверный. Ожидали: "{expected_title}", получили: "{actual_title}"'

                def test_ab_testing_page_decription(self, driver):
                    a_b_testing = AbTestingPage(driver)
                    a_b_testing.open(URL.A_B_TESTING_PAGE)
                    expected_description = a_b_testing.get_expected_description()
                    actual_description = a_b_testing.get_current_description()
                    assert expected_description == actual_description, f'Описание страницы неверное. Ожидали: "{expected_description}", получили: "{actual_description}"'