from selenium.webdriver.common.by import By


class AddPageLocators:
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, '.example button')
    DELETE_BUTTON = (By.CSS_SELECTOR, '#elements>button.added-manually')
    FIRST_DELETE_BUTTON = (By.CSS_SELECTOR, '#elements>button:first-child')
