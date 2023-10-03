from selenium.webdriver.common.by import By

from page_objects.checkout import CheckoutPage


class ShopPage:

    items_list = (By.XPATH,"//div[@class='card h-100']")
    checkout =(By.XPATH,"//a[@class='nav-link btn btn-primary']")
    second_checkout = (By.CLASS_NAME,"btn-success")

    def __init__(self,driver):
        self.driver = driver

    def select_item(self):
        return self.driver.find_elements(*ShopPage.items_list)

    def click_checkout(self):
        return self.driver.find_element(*ShopPage.checkout)

    def confirm_checkout(self):
        self.driver.find_element(*ShopPage.second_checkout).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

