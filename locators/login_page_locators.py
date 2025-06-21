from selenium.webdriver.common.by import By


class LoginLocators:

    LOCATOR_FIELD_EMAIL_LOGIN = By.XPATH, "//input[@type='text']"
    LOCATOR_FIELD_PASSWORD_LOGIN = By.XPATH, "//input[@type='password']"
    LOCATOR_BUTTON_LOGIN = By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']"