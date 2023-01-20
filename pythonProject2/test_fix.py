import  pytest

## pytest -rA .\test_custom_markers.py -m regression
## pytest -rA .\test_custom_markers.py -m smoke
## pytest -rA .\test_custom_markers.py -m "smoke and regression"
## pytest -rA .\test_custom_markers.py -m "smoke or regression"
## pytest -rA .\test_custom_markers.py -m "bhagyashree"

import time

@pytest.mark.smoke
def test_1():
    x = 10
    y = 20
    assert x == y   # assert is like comparision if its result is true then test case is passed if false then test case is failed


@pytest.mark.regression
def test_2():
    x = 20
    y = 20
    assert x == y


@pytest.mark.regression
def test_t3():
    x = 10
    y = 20
    result = x + y
    assert result == 30


@pytest.mark.regression
@pytest.mark.smoke
def test_t4():
    x = 10
    y = 20
    result = x + y
    assert result == 30


@pytest.mark.bhagyashree
def test_check_in():
    name = "Credence"
    message = "Credence is the best place to learn and also extended family"
    assert name in message  ## in =>  like operator or contains function


@pytest.mark.regression
def test_check_is():
    name = "Credence"
    message = "Credence is the best place to learn and also extended family"
    assert name is message  # is =>  equal to



@pytest.fixture
def setup():
    print("get driver")
    print("maximize window")
    yield       ### divide before and after activity
    print("print title")
    print("close window")


def test_facebook_login(setup):
    print("open facebook url")


def test_amazon_login(setup):
    print("open amazon url")

def test_flipkart_login(setup):
    print("open flipkart url")

def test_gmail_login(setup):
    print("open gmail url")



### pytest -rA .\test_fixture_selenium.py -n 4


from selenium import webdriver

driver = None


@pytest.fixture
def setup():
    global driver ## global => to access it outside function
    ## do not create local copy of variable use global variable from outside funciton
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield   ## divide before and after activity
    print(driver.title)
    time.sleep(10)
    driver.close()


def test_1(setup):
    driver.get("https://facebook.com")
    ## other test logic to login facebook


def test_2(setup):
    driver.get('https://gmail.com')
    ## other test logic


def test_3(setup):
    driver.get('https://amazon.com')
    ## other test logic

def test_4(setup):
    driver.get('https://flipkart.com')
    ## other test logic
