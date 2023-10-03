from selenium.webdriver.common.by import By

from page_objects.shop import ShopPage


class HomePage():

    shop = (By.LINK_TEXT,"Shop") #class variable -tuple of selector and actual value

    reg_name = (By.CSS_SELECTOR,"input[name='name']")
    reg_email = (By.NAME,"email")
    reg_checkbox = (By.ID,"exampleCheck1")
    reg_gender = (By.ID, "exampleFormControlSelect1")
    reg_occupation = (By.ID, "inlineRadio1")
    reg_submit = (By.XPATH,"//input[@type='submit']")
    reg_assert_msg = (By.CLASS_NAME,"alert-success")

    def __init__(self,driver):
        self.driver = driver

    def click_shop(self):
        self.driver.find_element(*HomePage.shop).click()#passing class variable shop with *(to deserialize the tuple)
        shopPage = ShopPage(self.driver)
        return shopPage

    #registration page...
    def get_name(self):
        return self.driver.find_element(*HomePage.reg_name)

    def get_email(self):
        return self.driver.find_element(*HomePage.reg_email)

    def select_checkbox(self):
        return self.driver.find_element(*HomePage.reg_checkbox)

    def select_gender(self):
        return self.driver.find_element(*HomePage.reg_gender)

    def select_occupation(self):
        return self.driver.find_element(*HomePage.reg_occupation)

    def submit(self):
        return self.driver.find_element(*HomePage.reg_submit)

    def assert_success_msg(self):
        return self.driver.find_element(*HomePage.reg_assert_msg)