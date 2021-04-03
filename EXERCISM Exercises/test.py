import pytest
import requests
import json


# def func(x):
#     return x + 5

# def test_method():
#     assert func(3) == 5


# def test_method1():
#     x = 5
#     y = 10
#     assert x == y

# def test_method2():
#     a = 15
#     b = 20
#     assert a+5 == b

def main_url():
    return "http://api.open-notify.org/iss-now.json"


def test_valid_login():
    url = 