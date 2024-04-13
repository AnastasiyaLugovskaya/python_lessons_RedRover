import requests


def check_page_response(url):
    """this method is used to check page response"""
    response = requests.get(url)
    return response


def get_names_of_goods(goods_list):
    """this method is used to get names of goods in a list"""
    name_items = [i.text for i in goods_list]
    return name_items


def get_prices_of_goods(goods_list):
    """this method is used to get prices of goods in a list"""
    good_prices = [float(i.text[1:]) for i in goods_list]
    return good_prices


def sort_list(lst: list, reverse_option):
    """this method is used to sort a list"""
    return sorted(lst, reverse=reverse_option)
