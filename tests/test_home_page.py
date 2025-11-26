import pytest
from urls.links import URL
URL = URL

class TestHomePage:
    
    @pytest.mark.smoke_home_page
    class TestSmokeHomePage:
        """
        Общие смоук тесты для страницы HomePage
        """

        def test_is_home_page_opened(self, home_page):
            home_page.open(URL.HOME_PAGE)
            home_page.is_page_loaded(URL.HOME_PAGE)
    
    class TestRegressHomePage:
        pass
