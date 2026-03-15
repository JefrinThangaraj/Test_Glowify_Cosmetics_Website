from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open_url(self, url):
        self.driver.get(url)
        time.sleep(2)
    
    def enter_user_email(self, email):
        """Enter email in login form"""
        try:
            field = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
            field.clear()
            field.send_keys(email)
        except:
            try:
                field = self.wait.until(EC.presence_of_element_located((By.ID, "id_email")))
                field.clear()
                field.send_keys(email)
            except:
                pass
    
    def enter_user_password(self, password):
        """Enter password in login form"""
        try:
            field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            field.clear()
            field.send_keys(password)
        except:
            try:
                field = self.wait.until(EC.presence_of_element_located((By.ID, "id_password")))
                field.clear()
                field.send_keys(password)
            except:
                pass
    
    def click_rementer(self):
        """Click remember me checkbox"""
        try:
            cb = self.wait.until(EC.element_to_be_clickable((By.NAME, "remember")))
            cb.click()
        except:
            try:
                cb = self.wait.until(EC.element_to_be_clickable((By.ID, "id_remember")))
                cb.click()
            except:
                pass
    
    def click_login(self):
        """Click login button"""
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            btn.click()
        except:
            try:
                btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.auth-btn")))
                btn.click()
            except:
                pass