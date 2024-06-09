import os

import pytest


@pytest.fixture
def get_test_name():
    test_name = os.environ.get('PYTEST_CURRENT_TEST')
    return test_name.split(':')[-1].split(' ')[0]