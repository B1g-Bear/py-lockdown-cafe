import datetime

import pytest

from cafe import Cafe
from main import go_to_cafe


def test_go_to_cafe_all_ok():
    friends = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
    ]
    cafe = Cafe("KFC")
    assert go_to_cafe(friends, cafe) == "Friends can go to KFC"


def test_go_to_cafe_not_vaccinated():
    friends = [
        {
            "name": "Alisa",
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
    ]
    cafe = Cafe("KFC")
    assert go_to_cafe(friends, cafe) == "All friends should be vaccinated"


def test_go_to_cafe_need_masks():
    friends = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False,
        },
    ]
    cafe = Cafe("KFC")
    assert go_to_cafe(friends, cafe) == "Friends should buy 2 masks"
