from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random
import pytest

browser = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
accepted_usernames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user',
                      'error_user', 'visual_user']
PASSWORD = 'secret_sauce'


def login():
    """this method is used to log in user in system"""
    browser.get(base_url)
    username_field = browser.find_element(By.ID, 'user-name')
    username_field.send_keys(random.choice(accepted_usernames))
    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys(PASSWORD)
    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()


def add_good_to_basket_from_catalogue():
    """this method is used to add the first good on the catalogue page to basket"""
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR,
                                                'div#inventory_container.inventory_container>div>div:first-child button')
    add_to_basket_button.click()


def go_to_good_page():
    """this method is used to move to the page of the first good in the catalogue"""
    good_title = browser.find_element(By.CSS_SELECTOR, '.inventory_list div:first-child .inventory_item_description '
                                                       'div.inventory_item_name')
    good_title.click()


def add_good_to_basket_from_good_page():
    """this method is used for adding a good to basket from the good page"""
    add_button = browser.find_element(By.CSS_SELECTOR, '.inventory_details_desc_container button')
    add_button.click()


@pytest.mark.positive_path
@pytest.mark.auth
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


@pytest.mark.auth
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


@pytest.mark.positive_path
@pytest.mark.basket
def test_add_good_to_basket():
    login()
    add_good_to_basket_from_catalogue()
    basket_badge = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert basket_badge.text == '1'
    browser.quit()


@pytest.mark.positive_path
@pytest.mark.basket
def test_remove_good_from_basket():
    login()
    add_good_to_basket_from_catalogue()
    basket_link = browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
    basket_link.click()
    remove_button = browser.find_element(By.CSS_SELECTOR, '#cart_contents_container>div>div button.cart_button')
    remove_button.click()
    assert len(browser.find_elements(By.CSS_SELECTOR, '.cart_item')) == 0
    browser.quit()


@pytest.mark.good_page
def test_go_to_good_page_through_image():
    login()
    good_name = browser.find_element(By.CSS_SELECTOR, '.inventory_list div:first-child .inventory_item_description '
                                                      'div.inventory_item_name').text
    good_image = browser.find_element(By.CSS_SELECTOR, '#inventory_container>div>div:first-child '
                                                       '>div.inventory_item_img>a')
    good_image.click()
    assert browser.find_element(By.CLASS_NAME, 'inventory_details_name').text == good_name
    browser.quit()


@pytest.mark.good_page
def test_go_to_good_page_through_title():
    login()
    good_title = browser.find_element(By.CSS_SELECTOR, '.inventory_list div:first-child .inventory_item_description '
                                                      'div.inventory_item_name')
    good_name = good_title.text
    good_title.click()
    assert browser.find_element(By.CLASS_NAME, 'inventory_details_name').text == good_name
    browser.quit()


@pytest.mark.basket
@pytest.mark.good_page
def test_add_good_to_basket_from_good_page():
    login()
    go_to_good_page()
    add_good_to_basket_from_good_page()
    basket_badge = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert basket_badge.text == '1'
    browser.quit()


@pytest.mark.basket
@pytest.mark.good_page
def test_remove_good_from_good_page():
    login()
    go_to_good_page()
    add_good_to_basket_from_good_page()
    remove_button = browser.find_element(By.CSS_SELECTOR, '.inventory_details_desc_container button')
    remove_button.click()
    assert len(browser.find_elements(By.CSS_SELECTOR, '.shopping_cart_link span')) == 0
    browser.quit()

