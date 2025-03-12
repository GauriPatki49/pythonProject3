from selenium.webdriver.common.by import By


class ConfirmPage:
    
    def __init__(self, driver):
        self.driver = driver
    
    LocationName = (By.LINK_TEXT, "India")
    IAgreeButton = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    SubmitButton = (By.CSS_SELECTOR, "[type='submit']")
    SuccessText = (By.CLASS_NAME, 'alert-success alert-dismissible')
    
    def getDeliveryItem(self):
        return self.driver.find_element(*ConfirmPage.LocationName)
    
    def ConfirmPageButton(self):
        return self.driver.find_element(*ConfirmPage.IAgreeButton)
    
    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.SubmitButton)
    
    def successText(self):
        return self.driver.find_element(*ConfirmPage.SuccessText)
