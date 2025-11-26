import pytest
from urls.links import URL
URL = URL



class TestAbTestingPage:
    
    @pytest.mark.smoke_ab_testing_page
    class TestSmokeAbTestingPage:
        """
        Общие смоук тесты для страницы AbTestingPage
        """

        def test_is_home_page_opened(self, home_page):
            home_page.open(URL.A_B_TESTING_PAGE)
            assert home_page.is_page_loaded(URL.A_B_TESTING_PAGE)