from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
    
    CardTitle = (By.XPATH, "//div[@class='card h-100']")
    CardFooter = (By.XPATH, "//app-card[4]//div[1]//div[2]")
    CheckOut = (By.XPATH, "//button[@class='btn btn-success']")
    
    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.CardTitle)
    
    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.CardFooter)
    
    def getCheckOutItems(self):
        self.driver.find_element(*CheckOutPage.CheckOut)
        confirmPage = ConfirmPage(self.driver)
        return confirmPage



