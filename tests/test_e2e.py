
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        checkOutPage = CheckOutPage(self.driver)
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()
        for product in cards:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                checkOutPage.getCardFooter().click()
                self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmPage = checkOutPage.checkOutItems().click()
        log.name("country name as a Ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifyLinkPresence("India")
        ConfirmPage.getDeliveryItem().click()
        ConfirmPage.ConfirmPageButton().click()
        ConfirmPage.getSubmitButton().click()
        successText = ConfirmPage.SuccessText().text
        log.info("text received from application is" + successText)
        assert "Success! Thank you!" in successText
        
