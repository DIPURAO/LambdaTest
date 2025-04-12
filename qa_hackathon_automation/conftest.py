import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def driver(request):
    username = os.getenv("LT_USERNAME")
    access_key = os.getenv("LT_ACCESS_KEY")

    lt_options = {
        "LT:Options": {
            "user": username,
            "accessKey": access_key,
            "build": "QA Hackathon Build",
            "name": "QA Tests",
            "platformName": "Windows 10",
            "selenium_version": "4.0.0"
        },
        "browserName": "Chrome",
        "browserVersion": "latest"
    }

    options = webdriver.ChromeOptions()
    options.set_capability("LT:Options", lt_options["LT:Options"])
    driver = webdriver.Remote(
        command_executor=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub",
        options=options
    )
    yield driver
    driver.quit()
