from selenium.webdriver.common.by import By
class TestLocators:
    FIELD_NAME = By.XPATH, "(//input[@name = 'name'])[1]"
    FIELD_EMAIL_REGISTRATION = By.XPATH, "(//input[@name = 'name'])[2]"
    FIELD_EMAIL_LOGIN = By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text']"
    FIELD_PASSWORD = By.XPATH, "//input[@type='password']"

    BUTTON_REGISTRATION = By.XPATH, "//button[text()='Зарегистрироваться']"
    BUTTON_LOGIN = By.XPATH, "//button[text()='Войти']"
    BUTTON_ACCOUNT_LOGIN = By.XPATH, "//button[text()='Войти в аккаунт']"
    BUTTON_PLACE_ORDER = By.XPATH, "//button[text()='Оформить заказ']"
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']"
    BUTTON_LOGIN_PAGE_REGISTRATION = By.XPATH, "// a[ @ href = '/login']"
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']"
    BUTTON_EXIT = By.XPATH, "//button[text()='Выход']"
    LOGO = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']"
    BUTTON_FILING = By.XPATH, "//span[text()='Начинки']"
    BUTTON_SAUCE = By.XPATH, "//span[text()='Соусы']"

    BUTTON_BREAD = By.XPATH, "//span[text()='Булки']"

    PASSWORD_ERROR_MESSAGE = By.XPATH, "//p[@class='input__error text_type_main-default']"
    PERSONAL_ACCOUNT_TEXT = By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']"
    CONSTRUCTOR_TEXT = By.XPATH, "//h1[text()='Соберите бургер']"
    FILING_TEXT = By.XPATH, "//h2[text()='Начинки']"
    BREAD_TEXT = By.XPATH, "//h2[text()='Булки']"
    SAUCE_TEXT = By.XPATH, "//h2[text()='Соусы']"