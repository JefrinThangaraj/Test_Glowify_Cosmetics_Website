from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    FULLNAME_INPUT = (By.NAME, "fullname") 
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password1") 
    REMEMBER_CHECKBOX = (By.NAME, "remember")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button.auth-btn")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".errorlist, .alert-danger")
    PASSWORD_TOGGLE = (By.CSS_SELECTOR, ".toggle-pass")
    
    def open_signup_page(self):
        """Open the signup page"""
        self.driver.get("https://glowify-cosmetics-site.onrender.com/accounts/signup/")
        time.sleep(2)
    
    def enter_fullname(self, fullname):
        try:
            field = self.wait.until(EC.presence_of_element_located(self.FULLNAME_INPUT))
            field.clear()
            field.send_keys(fullname)
            return True
        except:
            try:
                field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
                field.clear()
                field.send_keys(fullname)
                return True
            except:
                return False
    
    def enter_email(self, email):
        try:
            field = self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))
            field.clear()
            field.send_keys(email)
            return True
        except:
            return False
    
    def enter_password(self, password):
        try:
            field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
            field.clear()
            field.send_keys(password)
            return True
        except:
            try:
                field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
                field.clear()
                field.send_keys(password)
                return True
            except:
                return False
    
    def click_remember_me(self):
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable(self.REMEMBER_CHECKBOX))
            checkbox.click()
            return True
        except:
            return False
    
    def click_register(self):
        try:
            register_btn = self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON))
            register_btn.click()
            time.sleep(2)
            return True
        except:
            return False
    
    def get_error_message(self):
        try:
            error = self.driver.find_element(*self.ERROR_MESSAGE)
            return error.text
        except:
            return None
    
    def is_registration_successful(self):
        current_url = self.driver.current_url.lower()
        return "signup" not in current_url
    
    def toggle_password_visibility(self):
        try:
            toggle = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_TOGGLE))
            toggle.click()
            return True
        except:
            return False
    
    def get_password_field_type(self):
        try:
            password_field = self.driver.find_element(*self.PASSWORD_INPUT)
            return password_field.get_attribute("type")
        except:
            return None