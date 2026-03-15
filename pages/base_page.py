from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self,by,locator):
        return self.driver.find_element(by, locator)

    def send_keys(self, by, locator, text):
        element = self.find_element(by, locator)
        element.clear()
        element.send_keys(text)
    
    def visit(self, url):
        self.driver.get(url)
    
    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None
    
    def find_elements(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []
    
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return True
        except:
            try:
                element = self.find_element(locator)
                if element:
                    self.driver.execute_script("arguments[0].click();", element)
                    return True
            except:
                return False
            return False
    
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text if element else ""
    
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def is_element_displayed(self, locator):
        element = self.find_element(locator)
        return element.is_displayed() if element else False
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return True
        return False
    
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)