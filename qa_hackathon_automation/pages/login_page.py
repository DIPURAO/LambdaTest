from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.enter_text(By.ID, "username", username)
        self.enter_text(By.ID, "password", password)
        self.click(By.CSS_SELECTOR, "button.radius")

    def get_flash_message(self):
        return self.get_text(By.ID, "flash")
