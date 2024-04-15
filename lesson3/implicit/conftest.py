from datetime import datetime

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def browser(chrome_options):
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    yield browser
    attach = browser.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {datetime.today}', attachment_type=allure.attachment_type.PNG)
    browser.quit()
