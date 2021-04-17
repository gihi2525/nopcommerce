from selenium import webdriver
from utilities.readProperties import ReadConfig
import pytest

#
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        selenium_path = ReadConfig.getChromeSeleniumPath()
        print("Launching Chrome browser")
        return webdriver.Chrome(executable_path=selenium_path)
    elif browser == "firefox":
        selenium_path = ReadConfig.getFirefoxSeleniumPath()
        print("Launching Firefox browser")
        return webdriver.Firefox(executable_path=selenium_path)
    elif browser == "edge":
        selenium_path = ReadConfig.getEdgeSeleniumPath()
        print("Launching Edge browser")
        return webdriver.Edge(executable_path=selenium_path)
    else:
        #default browser is chrome
        print("Launching Chrome browser")
        return webdriver.Chrome(executable_path=ReadConfig.getChromeSeleniumPath())

#thsi will get the value from CLI/hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

#this will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML report ###############


#it is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Custemer'
    config._metadata['Tester Name'] = 'Igal'

#it is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)