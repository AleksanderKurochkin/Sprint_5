from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

def generate_random_email():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{username}@{domain}.com"


class TestRegistration:

    def test_successful_registration_redirect_to_login_page(self, browser_chrome):
        browser_chrome.get("https://stellarburgers.nomoreparties.site/register")

        field_name = browser_chrome.find_element(*TestLocators.FIELD_NAME)
        field_email = browser_chrome.find_element(*TestLocators.FIELD_EMAIL_REGISTRATION)
        field_password = browser_chrome.find_element(*TestLocators.FIELD_PASSWORD)
        button_registration = browser_chrome.find_element(*TestLocators.BUTTON_REGISTRATION)

        field_name.send_keys('ivan0058')

        # Генерируем случайный email и вводим его в поле email
        random_email = generate_random_email()
        field_email.send_keys(random_email)

        field_password.send_keys('qwerrty1234')
        button_registration.click()

        wait = WebDriverWait(browser_chrome, 3)
        wait.until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        current_url = browser_chrome.current_url

        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_password_error_message_displayed(self, browser_chrome):
        browser_chrome.get("https://stellarburgers.nomoreparties.site/register")

        name = browser_chrome.find_element(*TestLocators.FIELD_NAME)
        email = browser_chrome.find_element(*TestLocators.FIELD_EMAIL_REGISTRATION)
        password = browser_chrome.find_element(*TestLocators.FIELD_PASSWORD)
        button_registration = browser_chrome.find_element(*TestLocators.BUTTON_REGISTRATION)

        name.send_keys('ivan0018')
        email.send_keys('ivan_0018@test.ru')
        password.send_keys('34')
        button_registration.click()

        wait = WebDriverWait(browser_chrome, 3)
        error_message = wait.until(EC.visibility_of_element_located(TestLocators.PASSWORD_ERROR_MESSAGE))

        assert error_message.text == 'Некорректный пароль'