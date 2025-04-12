from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AlertsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def load(self):
        self.driver.get(self.URL)

    def trigger_alert(self):
        self.click(By.XPATH, "//button[text()='Click for JS Alert']")
        return self.driver.switch_to.alert

    def trigger_confirm(self):
        self.click(By.XPATH, "//button[text()='Click for JS Confirm']")
        return self.driver.switch_to.alert

    def trigger_prompt(self):
        self.click(By.XPATH, "//button[text()='Click for JS Prompt']")
        return self.driver.switch_to.alert
