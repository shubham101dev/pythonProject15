import pytest

@pytest.fixture()
def data1():
    print("my name is shubham")
def data2(data1):
    print("my name is nikhil")
def data3(data1):
    print("my name is divya")
