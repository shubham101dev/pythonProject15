import pytest
from selenium import webdriver
@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver
# pytest -v -s -n=2 .\testcase\test_try.py
