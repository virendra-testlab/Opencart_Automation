from selenium.webdriver.common.by import By

class LoginPage:

    email_Name = "email"
    password_Id = "input-password"
    login_button = "//button[text() = 'Login']"
    txt_my_account = "//div[@id = 'content']/h1"

    def __init__(self, driver):
        self.driver = driver

    def EnterEmail(self, email):
        self.driver.find_element(By.NAME, self.email_Name).send_keys(email)

    def EnterPassword(self, pwd):
        self.driver.find_element(By.ID, self.password_Id).send_keys(pwd)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def getMyAccountText(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_my_account).is_displayed()
        except:
            return False