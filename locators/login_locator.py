from selenium.webdriver.common.by import By

class LoginLocator:

    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    REMEMBER_ME = (By.ID, "remember")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".auth-btn.mt-3")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".auth-btn.mt-3")
    NAME_ERROR = (By.ID, "nameError")
    EMAIL_ERROR = (By.ID, "emailError")
    PASSWORD_ERROR = (By.ID, "passwordError")
    USER_EMAIL_INPUT = (By.NAME, "email")
    USER_PASSWORD_INPUT = (By.NAME, "password")