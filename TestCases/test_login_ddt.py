import os.path
from time import sleep
from datetime import datetime
import Utilities.excelReadFile
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.MyAccountPage import MyAccountPage
from Utilities import excelReadFile
from Utilities import readProperties

class Test_Login_ddt:

    baseUrl = readProperties.ReadConfig.getApplicationUrl()
    excell_file_path = os.path.abspath(os.curdir)+"//TestData//"+"login_testdata.xlsx"

    def test_003_login_ddt(self, setup):
        self.total_rows = Utilities.excelReadFile.getTotalRows(self.excell_file_path, 'Sheet1')
        self.total_col = Utilities.excelReadFile.getTotalColumns(self.excell_file_path, "Sheet1")

        # browser setup
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        # Create objects of Pages
        self.hp = HomePage(self.driver)
        self.lg = LoginPage(self.driver)
        self.myAc = MyAccountPage(self.driver)

        # Get login user from excell sheet and login
        for rows in range(2,self.total_rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()
            self.email = excelReadFile.getReadData(self.excell_file_path, 'Sheet1', rows, 1)
            self.password = excelReadFile.getReadData(self.excell_file_path, 'Sheet1', rows, 2)

            self.lg.EnterEmail(self.email)
            self.lg.EnterPassword(self.password)
            self.lg.clickLoginButton()
            sleep(2)


            login_successful_text = self.lg.getMyAccountText()
            self.timestapmp =  datetime.now().strftime("%Y%m%d_%H%M%S")
            if login_successful_text != True:
                self.driver.save_screenshot(os.path.abspath(os.curdir)+"//Screenshots//"+f"unsuccessful_login_{self.timestapmp}.png")
                assert False
                self.driver.close()
            else:
                # Scrolling the page till logout link element
                capture_logout_text = self.myAc.LogoutText()
                self.driver.execute_script("arguments[0].scrollIntoView();", capture_logout_text)
                sleep(2)
                # click logout link of my account page
                self.myAc.ClickLogoutLink()
        self.driver.close()


