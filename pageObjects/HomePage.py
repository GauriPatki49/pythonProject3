from selenium.webdriver.common.by import By

from tests.test_e2e import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.CSS_SELECTOR, "input[name='name']")
    check = (By.ID, "examplecheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class='alert-success']")
    
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
    
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    
    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)
    
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)
    
    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)