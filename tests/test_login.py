from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    def test_login_using_button_login_account(self, browser_chrome):
        browser_chrome.get("https://stellarburgers.nomoreparties.site")

        wait = WebDriverWait(browser_chrome, 10)
        button_account_login = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT_LOGIN))
        button_account_login.click()

        field_email = wait.until(EC.visibility_of_element_located(TestLocators.FIELD_EMAIL_LOGIN))
        field_password = wait.until(EC.visibility_of_element_located(TestLocators.FIELD_PASSWORD))
        button_login = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN))

        field_email.send_keys('ivan_0052@test.ru')
        field_password.send_keys('qwerrty1234')
        button_login.click()

        button_place_order_locator = TestLocators.BUTTON_PLACE_ORDER
        button_place_order = wait.until(EC.visibility_of_element_located(button_place_order_locator))

        assert button_place_order.is_displayed()

    def test_login_using_button_login_registration_page(self, browser_chrome):
        browser_chrome.get("https://stellarburgers.nomoreparties.site/register")

        wait = WebDriverWait(browser_chrome, 10)
        button_login_page_registration = wait.until(
            EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN_PAGE_REGISTRATION))
        button_login_page_registration.click()

        field_email = wait.until(EC.visibility_of_element_located(TestLocators.FIELD_EMAIL_LOGIN))
        field_password = wait.until(EC.visibility_of_element_located(TestLocators.FIELD_PASSWORD))
        button_login = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN))

        field_email.send_keys('ivan_0052@test.ru')
        field_password.send_keys('qwerrty1234')
        button_login.click()

        button_place_order_locator = TestLocators.BUTTON_PLACE_ORDER
        button_place_order = wait.until(EC.visibility_of_element_located(button_place_order_locator))

        assert button_place_order.is_displayed()

    def test_login_using_button_login_forgot_password_page(self, browser_chrome):
        browser_chrome.get("https://stellarburgers.nomoreparties.site/forgot-password")

        wait = WebDriverWait(browser_chrome, 10)
        button_login_page_registration = wait.until(
            EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN_PAGE_REGISTRATION))
        button_login_page_registration.click()

        field_email = wait.until(EC.visibility_of_element_located(TestLocators.FIELD_EMAIL_LOGIN))
        field_password = wait.until(EC.visibility_of_element_located(TestLocators.FIELD_PASSWORD))
        button_login = wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN))

        field_email.send_keys('ivan_0052@test.ru')
        field_password.send_keys('qwerrty1234')
        button_login.click()

        button_place_order_locator = TestLocators.BUTTON_PLACE_ORDER
        button_place_order = wait.until(EC.visibility_of_element_located(button_place_order_locator))

        assert button_place_order.is_displayed()

    def test_login_using_button_personal_account(self, browser_chrome):
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

        button_place_order_locator = TestLocators.BUTTON_PLACE_ORDER
        button_place_order = wait.until(EC.visibility_of_element_located(button_place_order_locator))

        assert button_place_order.is_displayed()