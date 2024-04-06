from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.about_page_locators import AboutPage
from locators.auth_page_locators import AuthorizationPage
from locators.basket_page_locators import BasketPage
from locators.burger_menu_locators import BurgerMenu
from locators.catalogue_page_locators import CataloguePage
from locators.good_page_locators import GoodPage
from locators.header_menu_locators import HeaderMenu
from locators.order_page_locators import OrderPage
from data.urls import Url
from data.user_data import UserData
import random
import pytest
from faker import Faker


def login(browser):
    """this method is used to log in user in system"""
    browser.get(Url.BASE_URL)

    username_field = browser.find_element(*AuthorizationPage.USERNAME_FIELD)
    username_field.clear()
    username_field.send_keys(random.choice(UserData.ACCEPTED_USERNAMES))

    password_field = browser.find_element(*AuthorizationPage.PASSWORD_FIELD)
    password_field.clear()
    password_field.send_keys(UserData.PASSWORD)

    login_button = browser.find_element(*AuthorizationPage.LOGIN_BUTTON)
    login_button.click()


def add_good_to_basket_from_catalogue(browser):
    """this method is used to add the first good on the catalogue page to basket"""
    add_to_basket_button = browser.find_element(*CataloguePage.ADD_TO_BASKET_BUTTON)
    add_to_basket_button.click()


def go_to_good_page(browser):
    """this method is used to move to the page of the first good in the catalogue"""
    good_title = browser.find_element(*CataloguePage.GOOD_TITLE)
    good_title.click()


def add_good_to_basket_from_good_page(browser):
    """this method is used for adding a good to basket from the good page"""
    add_button = browser.find_element(*GoodPage.ADD_BUTTON)
    add_button.click()


def go_to_basket(browser):
    """this method is used to move to basket page"""
    basket_link = browser.find_element(*HeaderMenu.BASKET_LINK)
    basket_link.click()


@pytest.mark.positive_path
@pytest.mark.auth
def test_positive_auth(browser):
    target_url = Url.CATALOGUE_URL
    login(browser)

    assert browser.current_url == target_url, "URLs don't match, user didn't log in"


@pytest.mark.auth
def test_negative_auth(browser):
    error_message = 'Epic sadface: Username and password do not match any user in this service'

    browser.get(Url.BASE_URL)

    username_field = browser.find_element(*AuthorizationPage.USERNAME_FIELD)
    username_field.send_keys('user')

    password_field = browser.find_element(*AuthorizationPage.PASSWORD_FIELD)
    password_field.send_keys('user')

    login_button = browser.find_element(*AuthorizationPage.LOGIN_BUTTON)
    login_button.click()
    try:
        error_container = browser.find_element(*AuthorizationPage.ERROR_CONTAINER)
    except NoSuchElementException:
        error_container = None
        print('There are no error container')

    assert error_container.text == error_message, "There's no error message, user logged in but shouldn't"


@pytest.mark.positive_path
@pytest.mark.basket
def test_add_good_to_basket(browser):
    login(browser)
    add_good_to_basket_from_catalogue(browser)

    basket_badge = browser.find_element(*HeaderMenu.BASKET_BADGE)
    assert basket_badge.text == '1', "There's no badge on the basket, a good wasn't added to basket"


@pytest.mark.positive_path
@pytest.mark.basket
def test_remove_good_from_basket(browser):
    login(browser)
    add_good_to_basket_from_catalogue(browser)
    go_to_basket(browser)

    remove_button = browser.find_element(*BasketPage.REMOVE_BUTTON)
    remove_button.click()
    assert len(browser.find_elements(*HeaderMenu.BASKET_BADGES)) == 0, \
        "There is still be a badge on the basket, a good wasn't remover from basket"


@pytest.mark.good_page
def test_go_to_good_page_through_image(browser):
    login(browser)

    good_name = browser.find_element(*CataloguePage.GOOD_TITLE).text
    good_image = browser.find_element(*CataloguePage.GOOD_IMAGE)
    good_image.click()
    assert browser.find_element(*GoodPage.GOOD_TITLE).text == good_name,\
        "The good name and expected name don't match, there is a wrong page opened"


@pytest.mark.good_page
def test_go_to_good_page_through_title(browser):
    login(browser)

    good_title = browser.find_element(*CataloguePage.GOOD_TITLE)
    good_name = good_title.text
    good_title.click()
    assert browser.find_element(*GoodPage.GOOD_TITLE).text == good_name, \
        "The good name and expected name don't match, there is a wrong page opened"


@pytest.mark.basket
@pytest.mark.good_page
def test_add_good_to_basket_from_good_page(browser):
    login(browser)
    go_to_good_page(browser)
    add_good_to_basket_from_good_page(browser)

    basket_badge = browser.find_element(*HeaderMenu.BASKET_BADGE)
    assert basket_badge.text == '1', "There's no badge on the basket, a good wasn't added to basket"


@pytest.mark.basket
@pytest.mark.good_page
def test_remove_good_from_good_page(browser):
    login(browser)
    go_to_good_page(browser)
    add_good_to_basket_from_good_page(browser)

    remove_button = browser.find_element(*GoodPage.REMOVE_BUTTON)
    remove_button.click()
    assert len(browser.find_elements(*HeaderMenu.BASKET_BADGES)) == 0, \
        "There is still be a badge on the basket, a good wasn't remover from basket"


@pytest.mark.order
@pytest.mark.positive_path
def test_make_order(browser):
    expected_message = 'Checkout: Complete!'
    fake = Faker()

    login(browser)
    add_good_to_basket_from_catalogue(browser)
    go_to_basket(browser)

    checkout_button = browser.find_element(*BasketPage.CHECKOUT_BUTTON)
    checkout_button.click()

    first_name_field = browser.find_element(*OrderPage.FIRSTNAME_FIELD)
    first_name_field.clear()
    first_name_field.send_keys(fake.name())

    last_name_field = browser.find_element(*OrderPage.LASTNAME_FIELD)
    last_name_field.clear()
    last_name_field.send_keys(fake.name())

    postal_code_field = browser.find_element(*OrderPage.POSTAL_CODE_FIELD)
    postal_code_field.clear()
    postal_code_field.send_keys(random.randint(100000, 999999))

    continue_button = browser.find_element(*OrderPage.CONTINUE_BUTTON)
    continue_button.click()

    finish_button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(OrderPage.FINISH_BUTTON))
    finish_button.click()

    successful_message = browser.find_element(*OrderPage.SUCCESSFUL_MESSAGE).text
    assert successful_message == expected_message, "There's no successful message, the order isn't completed"


@pytest.mark.filter
def test_filter_a_to_z(browser):
    login(browser)

    filter_icon = browser.find_element(*CataloguePage.FILTER_ICON)
    filter_icon.click()

    az_filter = browser.find_element(*CataloguePage.AZ_FILTER)
    az_filter.click()

    item_list = list(browser.find_elements(*CataloguePage.ITEM_LIST))
    name_items = [i.text for i in item_list]
    sorted_items = sorted(name_items)

    assert name_items == sorted_items, "Items aren't sorted according to filter option"


@pytest.mark.filter
def test_filter_z_to_a(browser):
    login(browser)

    filter_icon = browser.find_element(*CataloguePage.FILTER_ICON)
    filter_icon.click()

    za_filter = browser.find_element(*CataloguePage.ZA_FILTER)
    za_filter.click()

    item_list = list(browser.find_elements(*CataloguePage.ITEM_LIST))
    name_items = [i.text for i in item_list]
    sorted_items = sorted(name_items, reverse=True)

    assert name_items == sorted_items, "Items aren't sorted according to filter option"


@pytest.mark.filter
def test_filter_hi_to_low(browser):
    login(browser)

    filter_icon = browser.find_element(*CataloguePage.FILTER_ICON)
    filter_icon.click()

    hilo_filter = browser.find_element(*CataloguePage.HILO_FILTER)
    hilo_filter.click()

    item_list = list(browser.find_elements(*CataloguePage.PRICE_LIST))
    prices = [float(i.text[1:]) for i in item_list]
    sorted_items = sorted(prices, reverse=True)

    assert prices == sorted_items, "Items aren't sorted according to filter option"


@pytest.mark.filter
def test_filter_low_to_hi(browser):
    login(browser)

    filter_icon = browser.find_element(*CataloguePage.FILTER_ICON)
    filter_icon.click()

    lohi_filter = browser.find_element(*CataloguePage.LOHI_FILTER)
    lohi_filter.click()

    item_list = list(browser.find_elements(*CataloguePage.PRICE_LIST))
    prices = [float(i.text[1:]) for i in item_list]
    sorted_items = sorted(prices)

    assert prices == sorted_items, "Items aren't sorted according to filter option"


@pytest.mark.burger
def test_log_out(browser):
    login(browser)

    burger_menu = browser.find_element(*BurgerMenu.BURGER_MENU)
    burger_menu.click()

    logout_link = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(BurgerMenu.LOGOUT_LINK))
    logout_link.click()

    assert browser.current_url == Url.BASE_URL, "URLs don't match, logout didn't happen"


@pytest.mark.burger
@pytest.mark.xfail
def test_about_button(browser):
    login(browser)

    burger_menu = browser.find_element(*BurgerMenu.BURGER_MENU)
    burger_menu.click()

    about_link = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(BurgerMenu.ABOUT_LINK))
    about_link.click()

    assert browser.find_element(*AboutPage.BODY).text != '403 Forbidden', "There is an error on the page"


@pytest.mark.burger
def test_reset_app_state(browser):
    login(browser)
    add_good_to_basket_from_catalogue(browser)

    burger_menu = browser.find_element(*BurgerMenu.BURGER_MENU)
    burger_menu.click()

    reset_link = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(BurgerMenu.RESET_LINK))
    reset_link.click()

    assert len(browser.find_elements(*HeaderMenu.BASKET_BADGES)) == 0, \
        'There are still goods in the basket'
