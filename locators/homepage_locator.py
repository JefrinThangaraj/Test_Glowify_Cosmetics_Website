from selenium.webdriver.common.by import By

class HomeLocators:
    """Locators for Home Page"""
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".quick-add, .add-to-cart, button[type='submit']")
    CART_ICON = (By.CSS_SELECTOR, ".cart-icon a, .cart-link, a[href*='cart']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".product-card")