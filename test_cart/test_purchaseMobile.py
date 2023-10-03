from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.home import HomePage
from utilities.baseClass import BaseClass

# all testcases(methods) shud be in class(oops concept can be used)
#@pytest.mark.usefixtures("browser_access")
class TestMobileCart(BaseClass):

    def test_buy_mobile(self):
        log = self.getLogger()
        log.info("shopping for iphone")
        #1.clicking on shop tab
        #using self. as now driver is made class variable in conftest file
        #self.driver.find_element(By.LINK_TEXT,"Shop").click() commented for page object implementation
        homePage = HomePage(self.driver)
        shopPage = homePage.click_shop()
        #driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click() #regex in xpath .. use contains and give a part of string
        #driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click() #using regex in href.. use *

        #2.grabing the phones list and adding iphone to cart
        #shopPage = ShopPage(self.driver) optimized POM

        #mobiles_list = self.driver.find_elements(By.XPATH,"//div[@class='card h-100']") #POM(page obj mechanism)
        mobiles_list = shopPage.select_item()
        for mobile_data in mobiles_list:
            #print(mobile_data.find_element(By.XPATH,"div/h4/a").text)
            if mobile_data.find_element(By.XPATH,"div/h4/a").text == "iphone X":
                mobile_data.find_element(By.XPATH,"div[2]/button").click()

        #3. checkout
        #self.driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click() POM
        shopPage.click_checkout().click()
        #4.checkout -second page
        checkoutPage = shopPage.confirm_checkout()
        #5. select country (dynamic dropdown)
        #checkoutPage = CheckoutPage(self.driver) #optimized POM
        #self.driver.find_element(By.ID,"country").send_keys("in") POM
        checkoutPage.enter_country().send_keys("in")
        # explicit_wait = WebDriverWait(self.driver,20) this utility can be reused so moved to baseClass
        # explicit_wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        self.explicitwait_presence_of_item("India")
        #self.driver.find_element(By.LINK_TEXT,"India").click() POM
        checkoutPage.select_country().click()

        #6. purchase the product and assert for success msg
       # self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click() POM
        checkoutPage.select_terms_checkbox().click()
        #self.driver.find_element(By.XPATH,"//input[@value='Purchase']").click() POM
        checkoutPage.click_purchase().click()
        #success_msg = self.driver.find_element(By.CLASS_NAME,"alert-success").text POM
        success_msg = checkoutPage.assert_success_msg().text
        log.info(f"purchased iphone : {success_msg}")
        assert "Success! Thank you!" in success_msg
