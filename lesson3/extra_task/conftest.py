from datetime import datetime

import allure
import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    attach = browser.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {datetime.today}', attachment_type=allure.attachment_type.PNG)
    browser.quit()
