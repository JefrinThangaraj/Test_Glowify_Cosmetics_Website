from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.homepage_locator import HomeLocators
import time

class HomePage(BasePage):
    """Home Page Object Model"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomeLocators
    
    def open_home_page(self):
        """Open the home page"""
        self.driver.get("https://glowify-cosmetics-site.onrender.com/")
        time.sleep(2)
    
    def add_first_product_to_cart(self):
        """Add the first product to cart using multiple methods"""
        try:
            add_buttons = self.find_elements(self.locators.ADD_TO_CART_BTN)
            if add_buttons:
                self.scroll_to_element(self.locators.ADD_TO_CART_BTN)
                time.sleep(1)
                self.execute_script("arguments[0].click();", add_buttons[0])
                return True
            
            result = self.execute_script("""
                var buttons = document.querySelectorAll('.quick-add, .add-to-cart, button[type="submit"]');
                if(buttons.length > 0) {
                    buttons[0].click();
                    return true;
                }
                return false;
            """)
            return result
        except:
            return False
    
    def go_to_cart(self):
        """Navigate to cart page"""
        try:
            if self.click(self.locators.CART_ICON):
                time.sleep(2)
                return True
            
            self.driver.get("https://glowify-cosmetics-site.onrender.com/shop/cart/")
            time.sleep(2)
            return True
        except:
            return False
    
    def get_product_count(self):
        """Get number of products on page"""
        return len(self.find_elements(self.locators.PRODUCT_CARDS))