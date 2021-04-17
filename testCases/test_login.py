import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


#testing login func
class Test_no_1_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationPassword()

    logger = LogGen.loggen()

    #testing the home page
    def test_homePageTitle(self,setup):

        self.logger.info("*************test login no. 1**************")
        self.logger.info("*************verifying Home Page Title**************")
        self.driver = setup
        self.driver.get(self.baseURL)

        #actional title comparing
        act_title = self.driver.title
        if act_title ==  "Your store. Login":
            time.sleep(2)
            self.driver.close()
            self.logger.info("*************The Test has passed**************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************The Test has failed**************")
            assert False

    @pytest.mark.functionality
    #testing login with valid username and password
    def test_login(self,setup):

        self.logger.info("*********test no. 2***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #actional title comparing
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration": #n
            self.driver.close()
            self.logger.info("**************test has passed**************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****************test has failed****************")
            assert False
