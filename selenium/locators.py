class AboutPage:
    BODY = 'body'


class AuthorizationPage:
    ACCEPTED_USERNAMES = ['standard_user', 'problem_user', 'performance_glitch_user',
                          'error_user', 'visual_user']
    BASE_URL = 'https://www.saucedemo.com/'
    ERROR_CONTAINER = '.error-message-container>h3'
    LOGIN_BUTTON = 'login-button'
    PASSWORD = 'secret_sauce'
    PASSWORD_FIELD = 'password'
    USERNAME_FIELD = 'user-name'


class BasketPage:
    BASKET_BADGE = '.cart_item'
    CHECKOUT_BUTTON = 'checkout'
    CONTINUE_BUTTON = 'continue'
    FINISH_BUTTON = 'finish'
    FIRSTNAME_FIELD = 'first-name'
    LASTNAME_FIELD = 'last-name'
    POSTAL_CODE_FIELD = 'postal-code'
    REMOVE_BUTTON = '#cart_contents_container>div>div button.cart_button'
    SUCCESSFUL_MESSAGE = '.header_secondary_container>span.title'


class BurgerMenu:
    ABOUT_LINK = 'about_sidebar_link'
    BURGER_MENU = 'react-burger-menu-btn'
    LOGOUT_LINK = 'logout_sidebar_link'
    RESET_LINK = 'reset_sidebar_link'


class CataloguePage:
    ADD_TO_BASKET_BUTTON = 'div#inventory_container.inventory_container>div>div:first-child button'
    AZ_FILTER = 'option[value="az"]'
    CATALOGUE_URL = 'https://www.saucedemo.com/inventory.html'
    FILTER_ICON = 'product_sort_container'
    GOOD_IMAGE = '#inventory_container>div>div:first-child>div.inventory_item_img>a'
    GOOD_TITLE = '.inventory_list div:first-child .inventory_item_description div.inventory_item_name'
    HILO_FILTER = 'option[value="hilo"]'
    ITEM_LIST = 'inventory_item_name'
    LOHI_FILTER = 'option[value="lohi"]'
    ZA_FILTER = 'option[value="za"]'


class GoodPage:
    ADD_BUTTON = '.inventory_details_desc_container button'
    GOOD_TITLE = 'inventory_details_name'
    REMOVE_BUTTON = '.inventory_details_desc_container button'


class HeaderMenu:
    BASKET_BADGE = 'shopping_cart_badge'
    BASKET_BADGES = '.shopping_cart_link span'
    BASKET_LINK = 'shopping_cart_link'

