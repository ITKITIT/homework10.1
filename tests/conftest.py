import pytest


@pytest.fixture
def get_mask():
    return "1234 56** **** 3456"


@pytest.fixture
def get_data():
    return "11.03.2024"
