from selenium.webdriver.common.by import By

class CartLocators:
    
    CART_TITLE = (By.CSS_SELECTOR, "h2.cart-title")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item")
    ITEMS_COUNT = (By.ID, "selectedCount")
    
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".product-info h6")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".col-price")
    PRODUCT_TOTALS = (By.CSS_SELECTOR, ".row-total")
    QUANTITY_VALUES = (By.CSS_SELECTOR, ".qty-val")
    
    ITEM_CHECKBOXES = (By.CSS_SELECTOR, ".item-check")
    SELECTED_ITEMS = (By.ID, "selectedItems")
    
    SUBTOTAL = (By.ID, "subtotal")
    GRAND_TOTAL = (By.ID, "grandTotal")
    SHIPPING = (By.XPATH, "//div[contains(text(),'Estimated Shipping')]/following-sibling::span")
    GST = (By.XPATH, "//div[contains(text(),'GST')]/following-sibling::span")
    
    CHECKOUT_BTN = (By.CSS_SELECTOR, ".checkout-btn")
    
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".text-center h4")