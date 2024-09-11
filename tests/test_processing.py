import pytest

from src.processing import filter_by_state


@pytest.mark.parametrize(
    "list_dictionaries, state",
    [
        (
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
        ),
        ([{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], []),
        ([], []),
    ],
)
def test_filter_by_state(list_dictionaries, state):
    """Тест функции filter_by_state"""
    assert filter_by_state(list_dictionaries) == state
