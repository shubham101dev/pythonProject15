import pytest
@pytest.fixture()
def setup():
    print("once before every method")


def testmethod1(setup):
    print("this is test method 1")


def testmethod2(setup):
    print("this is test method2")


