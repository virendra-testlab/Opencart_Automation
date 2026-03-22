import os.path
import time

from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig

class Test_Login:
    url = ReadConfig.getApplicationUrl()
    emailAddress = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    actual_My_Account_text = "My Account"

    def test_003_Login_User(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lg = LoginPage(self.driver)
        self.lg.EnterEmail(self.emailAddress)
        self.lg.EnterPassword(self.password)
        self.lg.clickLoginButton()

        self.target_page = self.lg.getMyAccountText()

        if self.target_page == True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//Screenshots//"+"test_login_page.png")
            assert False
            self.driver.close()



