import os.path
from PageObjects.HomePage import HomePage
from PageObjects.RegistrationPageObject import RegistrationPage
from PageObjects.RegistrationSuccessPageObject import RegistrationSuccessPage
from PageObjects.MyAccountPage import MyAccountPage
from Utilities import RandomString
from Utilities.readProperties import ReadConfig
import pytest
from datetime import datetime
from time import sleep


class Test_RegistrationPageTest:
    baseUrl = ReadConfig.getApplicationUrl()


# this function check account registration and successful message
    def test_001_registration_successful(self, setup):
        # Driver setup
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.email = RandomString.random_email_generator() + "@gmail.com"
        # print("Title of Page: ", self.driver.title)

        # Click on Registration and open registration page
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        # print("Title of Registration Page", self.driver.title)
        sleep(3)
        # Entering valid data in the  Registration form

        self.reg = RegistrationPage(self.driver)
        self.reg.enterFirstName("Ankur")
        self.reg.enterLastName("Sharma")
        self.reg.enterEmail(self.email)
        self.reg.enterPassword("root@123")

        # Scroll the page till continue button
        policy_Webelement = self.reg.clickPolicy()
        self.driver.execute_script("arguments[0].scrollIntoView();", policy_Webelement)
        sleep(1)
        self.driver.execute_script("arguments[0].click();", policy_Webelement)
        # print(policy_Webelement.get_attribute("name"))
        self.reg.Regsitration_submit()
        sleep(3)
        # Validate Registration Successful
        self .reg_success = RegistrationSuccessPage(self.driver)
        Reg_success_text = self.reg_success.getSuccessMessage()
        # print("message: ", Reg_success_text)

        if Reg_success_text == "Your Account Has Been Created!":
            assert True
            self.reg_success.myAccount_continue_button()
            self.myAcc = MyAccountPage(self.driver)
            # Logout
            logout_link = self.myAcc.LogoutText()
            self.driver.execute_script("arguments[0].scrollIntoView();", logout_link)
            self.myAcc.ClickLogoutLink()
        else:
            self.timestapmp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//Screenshots//"+f"registration_error{self.timestapmp}.png")
            assert False

    @pytest.mark.sanity
    def test_002_Validate_Error(self, setup):

        # webdriver object setup
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)

        # Click on Register
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        # Navigate to Registration and Click continue button
        self.reg = RegistrationPage(self.driver)
        continue_Webelement = self.reg.continue_webelement()
        print("Webelement Value: ",continue_Webelement)
        self.driver.execute_script("arguments[0].scrollIntoView();", continue_Webelement)
        sleep(2)
        self.reg.Regsitration_submit()
        sleep(1)

        # Verify error messages visible
        error_policy = self.reg.errorPolicy()

        webelement_firtname = self.reg.firstName_webelement()
        self.driver.execute_script("arguments[0].scrollIntoView();", webelement_firtname)
        #sleep(1)
        assert self.reg.errorFirstName()    == True
        assert  self.reg.errorLastName()    == True
        assert self.reg.errorEmail()        == True
        assert self.reg.errorPassword()     == True
        assert error_policy                 == True