from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestButtonPersonalAccount:

    def test_login_in_personal_account(self, browser_chrome):
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


        text_locator = TestLocators.PERSONAL_ACCOUNT_TEXT
        expected_text = wait.until(EC.visibility_of_element_located(text_locator)).text

        assert expected_text == "В этом разделе вы можете изменить свои персональные данные"