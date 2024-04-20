from selenium.webdriver.common.by import By


class CheckboxPageLocators:
    CHECKBOXES_FORM = (By.CSS_SELECTOR, '#checkboxes')
    FIRST_CHECKBOX = (By.CSS_SELECTOR, 'input[type="checkbox"]:first-child')
    SECOND_CHECKBOX = (By.CSS_SELECTOR, 'input[type="checkbox"]:last-child')
