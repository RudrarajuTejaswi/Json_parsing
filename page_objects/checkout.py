from selenium.webdriver.common.by import By

class CheckoutPage:

    input_country = (By.ID,"country")
    country_name = (By.LINK_TEXT,"India")
    terms_checkbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.XPATH,"//input[@value='Purchase']")
    success_msg = (By.CLASS_NAME,"alert-success")

    def __init__(self,driver):
        self.driver = driver

    def enter_country(self):
        return self.driver.find_element(*CheckoutPage.input_country)

    def select_country(self):
        return self.driver.find_element(*CheckoutPage.country_name)

    def select_terms_checkbox(self):
        return self.driver.find_element(*CheckoutPage.terms_checkbox)

    def click_purchase(self):
        return self.driver.find_element(*CheckoutPage.purchase_button)

    def assert_success_msg(self):
        return self.driver.find_element(*CheckoutPage.success_msg)