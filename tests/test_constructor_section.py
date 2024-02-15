from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestConstructor:

    def test_button_filing(self, browser_chrome):
        browser_chrome.get("https://stellarburgers.nomoreparties.site")

        wait = WebDriverWait(browser_chrome, 10)
        button_filing = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_FILING))
        button_filing.click()

        text_locator = TestLocators.FILING_TEXT
        expected_text = wait.until(EC.visibility_of_element_located(text_locator)).text

        assert expected_text == "Начинки"

    def test_button_sauce(self, browser_chrome):
        browser_chrome.get("https://stellarburgers.nomoreparties.site")

        wait = WebDriverWait(browser_chrome, 10)
        button_sauce = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_SAUCE))
        button_sauce.click()

        text_locator = TestLocators.SAUCE_TEXT
        expected_text = wait.until(EC.visibility_of_element_located(text_locator)).text

        assert expected_text == "Соусы"

    def test_button_bread(self, browser_chrome):
        browser_chrome.get("https://stellarburgers.nomoreparties.site")


        wait = WebDriverWait(browser_chrome, 10)
        button_sauce = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_SAUCE))
        button_sauce.click()

        wait = WebDriverWait(browser_chrome, 10)
        button_bread = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_BREAD))
        button_bread.click()

        text_locator = TestLocators.BUTTON_BREAD
        expected_text = wait.until(EC.visibility_of_element_located(text_locator)).text

        assert expected_text == "Булки"