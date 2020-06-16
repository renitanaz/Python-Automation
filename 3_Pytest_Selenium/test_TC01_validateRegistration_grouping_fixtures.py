from selenium.webdriver import Chrome
import pytest

@pytest.fixture(scope="module")
def setpath():
    global driver
    path ="C:\\Users\\User\\OneDrive\\APIAutomation\\exe\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield
    driver.close()

def test_registration_valid_datag_fixture(setpath) :
    driver.get("http://thetestingworld.com/testing")
    driver.maximize_window()
    assert driver.current_url == "https://thetestingworld.com/testing"

def test_registration_valid_datag_conditional_fixture(setpath) :
    driver.get("http://thetestingworld.com/testing")
    driver.maximize_window()

def test_registration_invalid_datag_fixture(setpath) :
    driver.get("http://thetestingworld.com/testing")
    driver.maximize_window()