from selenium.webdriver.common.by import By

class MyAccountPage:

    lnk_logout_LinkText = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def LogoutText(self):
        logout_WebElement = self.driver.find_element(By.LINK_TEXT, self.lnk_logout_LinkText)
        return logout_WebElement


    def ClickLogoutLink(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_logout_LinkText).click()