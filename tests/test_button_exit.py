from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestButtonExit:

    def test_button_exit(self, browser_chrome):
        browser_chrome.get("https://stellarburgers.nomoreparties.site")

        wait = WebDriverWait(browser_chrome, 10)
        button_personal_account = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_PERSONAL_ACCOUNT))
        button_personal_account.click()

        field_email = wait.until(EC.visibility_of_element_located(TestLocators.FIELD_EMAIL_LOGIN))
        field_password = wait.until(EC.visibility_of_element_located(TestLocators.FIELD_PASSWORD))
        button_login = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN))

        field_email.send_keys('ivan_0052@test.ru')
        field_password.send_keys('qwerrty1234')
        button_login.click()

        wait = WebDriverWait(browser_chrome, 10)
        button_personal_account = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_PERSONAL_ACCOUNT))
        button_personal_account.click()

        wait = WebDriverWait(browser_chrome, 10)
        button_exit = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_EXIT))
        button_exit.click()


        wait = WebDriverWait(browser_chrome, 3)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        current_url = browser_chrome.current_url

        assert current_url == 'https://stellarburgers.nomoreparties.site/login'