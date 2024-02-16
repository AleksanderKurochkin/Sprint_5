import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
@pytest.fixture(scope="function")
def browser_chrome():
    service = Service(executable_path=ChromeDriverManager().install())
    browser_chrome = webdriver.Chrome(service=service)
    browser_chrome.set_window_size(1920, 1080)
    yield browser_chrome
    browser_chrome.quit()