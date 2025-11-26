from selenium import webdriver
from pages.home_page import HomePage
from pages.ab_testing_page import AbTestingPage
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def ab_testing_page(driver):
    return AbTestingPage(driver)