from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
@pytest.fixture()
def setup(request):
    request.cls.driver=webdriver.Chrome()
    request.cls.driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
    yield
    time.sleep(5)
    request.cls.driver.close()


