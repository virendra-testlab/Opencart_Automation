from selenium.webdriver.common.by import By

class RegistrationPage:

    # Input fields Locators
    txt_firstname_id    = "input-firstname"
    txt_lastname_id     = "input-lastname"
    txt_email_id        = "input-email"
    txt_password_id     = "input-password"
    btn_subscribe_id    =  "input-newsletter"
    btn_policy_name     =  "agree"
    btn_continue_xpath  =   "//*[text()= 'Continue']"
    success_reg_msg_xpath = '//h1[text() = "Your Account Has Been Created!"]'

    # declare variable for policy pop up text
    policy_message = "Warning: You must agree to the Privacy Policy!"

    # Input Error message locators
    firstname_error_id  =   "error-firstname"
    lastname_error_id   =   "error-lastname"
    email_error_id      =   "error-email"
    password_error_id   =   "error-password"
    policy_error_xpath  =   "//div[@class = 'alert alert-danger alert-dismissible']"

    # Class cnstructor
    def __init__(self, driver):
        self.driver = driver

# Action method
    def enterFirstName(self, fname):
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(fname)

    def enterLastName(self, lname):
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lname)

    def enterEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def enterPassword(self, pwd):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(pwd)

    def clickPolicy(self):
        checkbox = self.driver.find_element(By.NAME, self.btn_policy_name)
        return checkbox

    def continue_webelement(self):
        continue_button = self.driver.find_element(By.XPATH, self.btn_continue_xpath)
        return continue_button

    def Regsitration_submit(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def Registration_successful(self):
        return self.driver.find_element(By.XPATH, self.success_reg_msg_xpath).text

    # Error Message methods

    def errorFirstName(self):
        fn = self.driver.find_element(By.ID, self.firstname_error_id).is_displayed()
        return fn

    def errorLastName(self):
        ln = self.driver.find_element(By.ID, self.lastname_error_id).is_displayed()
        return ln

    def errorEmail(self):
        email = self.driver.find_element(By.ID, self.email_error_id).is_displayed()
        return email

    def errorPassword(self):
        pwd = self.driver.find_element(By.ID, self.password_error_id).is_displayed()
        return pwd
    def errorPolicy(self):
        pol = self.driver.find_element(By.XPATH, self.policy_error_xpath).is_displayed()
        return pol

    def firstName_webelement(self):
        firstname_webelement = self.driver.find_element(By.ID, self.txt_firstname_id)
        return firstname_webelement