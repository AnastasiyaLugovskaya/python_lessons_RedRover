from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.common.exceptions import NoSuchElementException
import random

import pytest

browser = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
accepted_usernames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user',
                      'error_user', 'visual_user']
PASSWORD = 'secret_sauce'



def test_positive_auth():
    target_url = 'https://www.saucedemo.com/inventory.html'
    browser.get(base_url)
    username_field = browser.find_element(By.ID, 'user-name')
    username_field.send_keys(random.choice(accepted_usernames))
    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys(PASSWORD)
    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()
    assert browser.current_url == target_url
    browser.quit()


def test_negative_auth():
    error_message = 'Epic sadface: Username and password do not match any user in this service'
    browser.get(base_url)
    username_field = browser.find_element(By.ID, 'user-name')
    username_field.send_keys('user')
    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys('user')
    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()
    try:
        error_container = browser.find_element(By.CSS_SELECTOR, '.error-message-container>h3')
    except NoSuchElementException:
        error_container = None
        print('There are no error container')
    assert error_container.text == error_message
    browser.quit()
