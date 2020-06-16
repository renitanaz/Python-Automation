from selenium.webdriver import Chrome
import pytest

@pytest.mark.skip("dont want to exe on current build")
def test_registration_valid_data() :
    path ="C:\\Users\\User\\OneDrive\\APIAutomation\\exe\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://thetestingworld.com/testing")
    driver.maximize_window()
a=100
@pytest.mark.skip(a>100,reason="dont want to exe on current build")
def test_registration_valid_data_conditional() :
    path ="C:\\Users\\User\\OneDrive\\APIAutomation\\exe\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://thetestingworld.com/testing")
    driver.maximize_window()

def test_registration_invalid_data() :
    path ="C:\\Users\\User\\OneDrive\\APIAutomation\\exe\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://thetestingworld.com/testing")
    driver.maximize_window()