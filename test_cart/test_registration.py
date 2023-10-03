import pytest

from page_objects.home import HomePage

from utilities.baseClass import BaseClass

class TestUserRegistration(BaseClass):

    def test_registerUser(self,get_data):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("entering data to the registration page")
        homePage.get_name().send_keys(get_data["firstname"])
        homePage.get_email().send_keys(get_data["email"])
        homePage.select_checkbox().click()
        self.select_dropdown_by_text(get_data["gender"], homePage.select_gender())
        homePage.select_occupation().click()
        homePage.submit().click()
        message = homePage.assert_success_msg().text
        log.info(f"user registration complete : {message}")
        assert "success" in message








