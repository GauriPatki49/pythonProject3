import pytest
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass, SelectOptionByText


class TestHomePage(BaseClass):
    
    @pytest.mark.regression
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is"+getData)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["LastName"])
        homepage.getCheckBox().click()
        self.SelectOptionByText(homepage.getGender(), getData["gender"])
        
        homepage.getSubmit().click()
        
        alertText = homepage.getSuccessMessage().text
        
        assert ("success" in alertText)
        self.driver.refresh()
    
    @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    def getData(self, request):
        return request.param
