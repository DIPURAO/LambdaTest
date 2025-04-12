import pytest
from pages.alerts_page import AlertsPage

def test_js_alert(driver):
    page = AlertsPage(driver)
    page.load()
    alert = page.trigger_alert()
    assert alert.text == "I am a JS Alert"
    alert.accept()

def test_js_confirm(driver):
    page = AlertsPage(driver)
    page.load()
    alert = page.trigger_confirm()
    assert alert.text == "I am a JS Confirm"
    alert.dismiss()

def test_js_prompt(driver):
    page = AlertsPage(driver)
    page.load()
    alert = page.trigger_prompt()
    assert alert.text == "I am a JS prompt"
    alert.send_keys("Test Input")
    alert.accept()
