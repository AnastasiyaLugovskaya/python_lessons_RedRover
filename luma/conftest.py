import pytest
from selene import browser, support
from selenium import webdriver
import allure_commons
import allure


@pytest.fixture(autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    browser.config.driver_options = options
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config._wait_decorator = support._logging.wait_with(
            context=allure_commons._allure.StepContext
        )
    yield
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )
    browser.quit()
