from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import pytest
from faker import Faker


base_url = 'https://www.saucedemo.com/'
accepted_usernames = ['standard_user',  'problem_user', 'performance_glitch_user',
                      'error_user', 'visual_user']
PASSWORD = 'secret_sauce'
fake = Faker()


def get_browser():
    """this method returns an instance of a browser"""
    return webdriver.Chrome()


def login(browser):
    """this method is used to log in user in system"""
    browser.get(base_url)

    username_field = browser.find_element(By.ID, 'user-name')
    username_field.clear()
    username_field.send_keys(random.choice(accepted_usernames))

    password_field = browser.find_element(By.ID, 'password')
    password_field.clear()
    password_field.send_keys(PASSWORD)

    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()


def add_good_to_basket_from_catalogue(browser):
    """this method is used to add the first good on the catalogue page to basket"""
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR,
                                                'div#inventory_container.inventory_container>div>div:first-child button')
    add_to_basket_button.click()


def go_to_good_page(browser):
    """this method is used to move to the page of the first good in the catalogue"""
    good_title = browser.find_element(By.CSS_SELECTOR, '.inventory_list div:first-child .inventory_item_description '
                                                       'div.inventory_item_name')
    good_title.click()


def add_good_to_basket_from_good_page(browser):
    """this method is used for adding a good to basket from the good page"""
    add_button = browser.find_element(By.CSS_SELECTOR, '.inventory_details_desc_container button')
    add_button.click()


def go_to_basket(browser):
    """this method is used to move to basket page"""
    basket_link = browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
    basket_link.click()


@pytest.mark.positive_path
@pytest.mark.auth
def test_positive_auth():
    browser = get_browser()
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
    browser = get_browser()
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
    browser = get_browser()

    login(browser)
    add_good_to_basket_from_catalogue(browser)

    basket_badge = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert basket_badge.text == '1'
    browser.quit()


@pytest.mark.positive_path
@pytest.mark.basket
def test_remove_good_from_basket():
    browser = get_browser()

    login(browser)
    add_good_to_basket_from_catalogue(browser)
    go_to_basket(browser)

    remove_button = browser.find_element(By.CSS_SELECTOR, '#cart_contents_container>div>div button.cart_button')
    remove_button.click()
    assert len(browser.find_elements(By.CSS_SELECTOR, '.cart_item')) == 0
    browser.quit()


@pytest.mark.good_page
def test_go_to_good_page_through_image():
    browser = get_browser()

    login(browser)

    good_name = browser.find_element(By.CSS_SELECTOR, '.inventory_list div:first-child .inventory_item_description '
                                                      'div.inventory_item_name').text
    good_image = browser.find_element(By.CSS_SELECTOR, '#inventory_container>div>div:first-child'
                                                       '>div.inventory_item_img>a')
    good_image.click()
    assert browser.find_element(By.CLASS_NAME, 'inventory_details_name').text == good_name
    browser.quit()


@pytest.mark.good_page
def test_go_to_good_page_through_title():
    browser = get_browser()

    login(browser)

    good_title = browser.find_element(By.CSS_SELECTOR, '.inventory_list div:first-child .inventory_item_description '
                                                      'div.inventory_item_name')
    good_name = good_title.text
    good_title.click()
    assert browser.find_element(By.CLASS_NAME, 'inventory_details_name').text == good_name
    browser.quit()


@pytest.mark.basket
@pytest.mark.good_page
def test_add_good_to_basket_from_good_page():
    browser = get_browser()

    login(browser)
    go_to_good_page(browser)
    add_good_to_basket_from_good_page(browser)

    basket_badge = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert basket_badge.text == '1'
    browser.quit()


@pytest.mark.basket
@pytest.mark.good_page
def test_remove_good_from_good_page():
    browser = get_browser()

    login(browser)
    go_to_good_page(browser)
    add_good_to_basket_from_good_page(browser)

    remove_button = browser.find_element(By.CSS_SELECTOR, '.inventory_details_desc_container button')
    remove_button.click()
    assert len(browser.find_elements(By.CSS_SELECTOR, '.shopping_cart_link span')) == 0
    browser.quit()


@pytest.mark.order
@pytest.mark.positive_path
def test_make_order():
    expected_message = 'Checkout: Complete!'
    browser = get_browser()

    login(browser)
    add_good_to_basket_from_catalogue(browser)
    go_to_basket(browser)

    checkout_button = browser.find_element(By.ID, 'checkout')
    checkout_button.click()

    first_name_field = browser.find_element(By.ID, 'first-name')
    first_name_field.clear()
    first_name_field.send_keys(fake.name())

    last_name_field = browser.find_element(By.ID, 'last-name')
    last_name_field.clear()
    last_name_field.send_keys(fake.name())

    postal_code_field = browser.find_element(By.ID, 'postal-code')
    postal_code_field.clear()
    postal_code_field.send_keys(random.randint(100000, 999999))

    continue_button = browser.find_element(By.ID, 'continue')
    continue_button.click()

    finish_button = browser.find_element(By.ID, 'finish')
    finish_button.click()

    successful_message = browser.find_element(By.CSS_SELECTOR, '.header_secondary_container>span.title').text
    assert successful_message == expected_message
    browser.quit()


@pytest.mark.filter
def test_filter_a_to_z():
    browser = get_browser()

    login(browser)

    filter_icon = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    filter_icon.click()

    az_filter = browser.find_element(By.CSS_SELECTOR, 'option[value="az"]')
    az_filter.click()

    item_list = list(browser.find_elements(By.CLASS_NAME, 'inventory_item_name'))
    name_items = [i.text for i in item_list]
    sorted_items = sorted(name_items)

    assert name_items == sorted_items
    browser.quit()


@pytest.mark.filter
def test_filter_z_to_a():
    browser = get_browser()

    login(browser)

    filter_icon = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    filter_icon.click()

    za_filter = browser.find_element(By.CSS_SELECTOR, 'option[value="za"]')
    za_filter.click()

    item_list = list(browser.find_elements(By.CLASS_NAME, 'inventory_item_name'))
    name_items = [i.text for i in item_list]
    sorted_items = sorted(name_items, reverse=True)

    assert name_items == sorted_items
    browser.quit()


@pytest.mark.filter
def test_filter_hi_to_low():
    browser = get_browser()

    login(browser)

    filter_icon = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    filter_icon.click()

    za_filter = browser.find_element(By.CSS_SELECTOR, 'option[value="hilo"]')
    za_filter.click()

    item_list = list(browser.find_elements(By.CLASS_NAME, 'inventory_item_price'))
    prices = [float(i.text[1:]) for i in item_list]
    sorted_items = sorted(prices, reverse=True)

    assert prices == sorted_items
    browser.quit()


@pytest.mark.filter
def test_filter_low_to_hi():
    browser = get_browser()

    login(browser)

    filter_icon = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    filter_icon.click()

    za_filter = browser.find_element(By.CSS_SELECTOR, 'option[value="lohi"]')
    za_filter.click()

    item_list = list(browser.find_elements(By.CLASS_NAME, 'inventory_item_price'))
    prices = [float(i.text[1:]) for i in item_list]
    sorted_items = sorted(prices)

    assert prices == sorted_items
    browser.quit()


@pytest.mark.burger
def test_log_out():
    browser = get_browser()

    login(browser)

    burger_menu = browser.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()

    logout_link = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
    logout_link.click()

    assert browser.current_url == base_url, "URLs don't match, logout didn't happen"
    browser.quit()


@pytest.mark.burger
@pytest.mark.xfail
def test_about_button():
    browser = get_browser()

    login(browser)

    burger_menu = browser.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()

    about_link = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, 'about_sidebar_link')))
    about_link.click()

    assert browser.find_element(By.TAG_NAME, 'body').text != '403 Forbidden', "There is an error on the page"
    browser.quit()
