from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.about_page_locators import AboutPageLocators
from locators.auth_page_locators import AuthorizationPageLocators
from locators.basket_page_locators import BasketPageLocators
from locators.burger_menu_locators import BurgerMenuLocators
from locators.catalogue_page_locators import CataloguePageLocators
from locators.good_page_locators import GoodPageLocators
from locators.header_menu_locators import HeaderMenuLocators
from locators.order_page_locators import OrderPageLocators
from data.urls import Url
from data.user_data import UserData
import random
import pytest
from faker import Faker



@pytest.mark.good_page
def test_go_to_good_page_through_image(browser):
    login(browser)

    good_name = browser.find_element(*CataloguePageLocators.GOOD_TITLE).text
    good_image = browser.find_element(*CataloguePageLocators.GOOD_IMAGE)
    good_image.click()
    assert browser.find_element(*GoodPageLocators.GOOD_TITLE).text == good_name,\
        "The good name and expected name don't match, there is a wrong page opened"


@pytest.mark.good_page
def test_go_to_good_page_through_title(browser):
    login(browser)

    good_title = browser.find_element(*CataloguePageLocators.GOOD_TITLE)
    good_name = good_title.text
    good_title.click()
    assert browser.find_element(*GoodPageLocators.GOOD_TITLE).text == good_name, \
        "The good name and expected name don't match, there is a wrong page opened"


@pytest.mark.basket
@pytest.mark.good_page
def test_remove_good_from_good_page(browser):
    login(browser)
    go_to_good_page(browser)
    add_good_to_basket_from_good_page(browser)

    remove_button = browser.find_element(*GoodPageLocators.REMOVE_BUTTON)
    remove_button.click()
    assert len(browser.find_elements(*HeaderMenuLocators.BASKET_BADGES)) == 0, \
        "There is still be a badge on the basket, a good wasn't remover from basket"



