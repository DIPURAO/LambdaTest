import pytest
from pages.login_page import LoginPage
from utils.credentials import Credentials

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Credentials.USERNAME, Credentials.PASSWORD)
    assert "You logged into a secure area!" in login_page.get_flash_message()

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wronguser", "wrongpass")
    assert "Your username is invalid!" in login_page.get_flash_message()
