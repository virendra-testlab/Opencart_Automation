from selenium.webdriver.common.by import By

class RegistrationSuccessPage:
    # locators
    SuccessMessage_xpath = '//h1[text()="Your Account Has Been Created!"]'
    continue_button_link = "Continue"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def getSuccessMessage(self):
        message = self.driver.find_element(By.XPATH, self.SuccessMessage_xpath).text
        return message

    def myAccount_continue_button(self):
        self.driver.find_element(By.LINK_TEXT, self.continue_button_link).click()