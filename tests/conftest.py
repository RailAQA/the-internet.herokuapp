from selenium import webdriver
from config.settings import settings
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.logging import logging
import pytest
import allure

#@pytest.fixture
#def driver():
 #   driver = webdriver.Chrome()
  #  driver.maximize_window()
   # yield driver
    #driver.close()

@pytest.fixture
def driver():
    if settings.BROWSER.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        
        # Максимальная попытка обхода ограничений
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-web-security')
        options.add_argument('--allow-running-insecure-content')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        driver = webdriver.Chrome(options=options)
    elif settings.BROWSER.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        logging.critical(f"Не поддерживаемый браузер: {settings.BROWSER}")
        raise ValueError(f"Не поддерживаемый браузер: {settings.BROWSER}")
    yield driver
    

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver and hasattr(driver, 'get_screenshot_as_png'):
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"screenshot_{item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                logging.warning(f"Не удалось сделать скриншот: {e}")