from selenium.webdriver import Chrome
import pytest

@pytest.mark.smoke
def test_registration_valid_datag() :
    path ="C:\\Users\\User\\OneDrive\\APIAutomation\\exe\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://thetestingworld.com/testing")
    driver.maximize_window()

@pytest.mark.sanity
def test_registration_valid_datag_conditional() :
    path ="C:\\Users\\User\\OneDrive\\APIAutomation\\exe\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://thetestingworld.com/testing")
    driver.maximize_window()

@pytest.mark.smoke
def test_registration_invalid_datag() :
    path ="C:\\Users\\User\\OneDrive\\APIAutomation\\exe\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://thetestingworld.com/testing")
    driver.maximize_window()