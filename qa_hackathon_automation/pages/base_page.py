from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by, value):
        self.wait.until(EC.element_to_be_clickable((by, value))).click()

    def enter_text(self, by, value, text):
        self.wait.until(EC.visibility_of_element_located((by, value))).send_keys(text)

    def get_text(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value))).text
