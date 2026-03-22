from selenium.webdriver.common.by import By

class HomePage:
    menu_myaccount_css = "//span[text() = 'My Account']"
    link_register_text = "Register"
    link_login_text = 'Login'

    def __init__(self, driver):
        self.driver = driver


    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,  self.menu_myaccount_css).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT, self.link_register_text).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.link_login_text).click()
