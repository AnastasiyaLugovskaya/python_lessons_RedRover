import pytest
import requests

base_url = 'https://restful-booker.herokuapp.com/booking'


@pytest.fixture(scope='function')
def auth_token():
    auth_url = 'https://restful-booker.herokuapp.com/auth'
    auth_data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_url, json=auth_data)
    token = response.json()['token']
    yield token


@pytest.fixture(scope='module')
def booking_id():
    payload = {
        "firstname": "Jimin",
        "lastname": "Park",
        "totalprice": 1500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-05-01",
            "checkout": "2024-05-15"
        },
        "additionalneeds": "Extra towels"
    }
    response = requests.post(base_url, json=payload)
    booking_id = response.json()['bookingid']
    yield booking_id


def test_check_deposit(auth_token, booking_id):
    response = requests.get(f'{base_url}/{booking_id}')
    is_deposit_paid = response.json()['depositpaid']
    assert is_deposit_paid 


def test_update_booking(auth_token, booking_id):
    payload = {
        "firstname": "Yoongi",
        "lastname": "Min",
        "totalprice": 1850,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-06-13",
            "checkout": "2025-06-20"
        },
        "additionalneeds": "ARMY Bomb must be in the room"
    }
    token = {'Cookie': f'token={auth_token}'}
    response = requests.put(f'{base_url}/{booking_id}', json=payload, headers=token)
    print(response)
    response_2 = requests.get(f'{base_url}/{booking_id}')
    client = response_2.json()['lastname'] + ' ' + response_2.json()['firstname']
    print(f'Factual client name is {client}')
    assert client == "Min Yoongi"


def test_update_booking_info(auth_token, booking_id):
    payload = {"bookingdates": {
        "checkin": "2025-06-13",
        "checkout": "2025-06-24"
    }
    }
    token = {'Cookie': f'token={auth_token}'}
    response = requests.patch(f'{base_url}/{booking_id}', json=payload, headers=token)
    new_dates = response.json()['bookingdates']
    new_checkout = new_dates['checkout']
    print(new_checkout)
    assert new_checkout == '2025-06-24'


def test_delete_booking(auth_token, booking_id):
    token = {'Cookie': f'token={auth_token}'}
    response = requests.delete(f'{base_url}/{booking_id}', headers=token)
    assert response.status_code == 201
    assert requests.get(f'{base_url}/{booking_id}').status_code == 404
