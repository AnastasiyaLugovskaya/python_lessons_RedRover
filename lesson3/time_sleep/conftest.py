import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def browser(chrome_options):
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()
