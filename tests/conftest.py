from selenium import webdriver
import pytest
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.failed:
        driver = item.funcargs.get('driver')
        if driver and hasattr(driver, 'get_screenshot_as_png'):
            # Скриншот
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"screenshot_{item.name}_{report.when}",
                attachment_type=allure.attachment_type.PNG
            )