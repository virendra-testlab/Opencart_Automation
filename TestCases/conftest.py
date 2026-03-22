import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Browser driver setup
@pytest.fixture(scope="class")
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

