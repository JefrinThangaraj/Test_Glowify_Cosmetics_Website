from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.cart_locator import CartLocators
import time

class CartPage(BasePage):
   
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartLocators
    
    def get_cart_title(self):
        return self.get_text(self.locators.CART_TITLE)
    
    def get_items_count(self):
        text = self.get_text(self.locators.ITEMS_COUNT)
        try:
            return int(text) if text else 0
        except:
            return 0
    
    def get_number_of_cart_items(self):
        return len(self.find_elements(self.locators.CART_ITEMS))
    
    def is_cart_empty(self):
        empty_msg = self.find_elements(self.locators.EMPTY_CART_MSG)
        return len(empty_msg) > 0
    
    def get_product_names(self):
        elements = self.find_elements(self.locators.PRODUCT_NAMES)
        return [el.text for el in elements if el]
    
    def get_product_prices(self):
        elements = self.find_elements(self.locators.PRODUCT_PRICES)
        prices = []
        for el in elements[1:]: 
            try:
                price_text = el.text.replace('₹', '').strip()
                if price_text:
                    prices.append(float(price_text))
            except:
                pass
        return prices
    
    def get_product_totals(self):
        elements = self.find_elements(self.locators.PRODUCT_TOTALS)
        totals = []
        for el in elements:
            try:
                total_text = el.text.strip()
                if total_text:
                    totals.append(float(total_text))
            except:
                pass
        return totals
    
    def get_quantities(self):
        elements = self.find_elements(self.locators.QUANTITY_VALUES)
        qtys = []
        for el in elements:
            try:
                qty_text = el.text.strip()
                if qty_text:
                    qtys.append(int(qty_text))
            except:
                pass
        return qtys
    
    def verify_product_calculations(self):
        prices = self.get_product_prices()
        qtys = self.get_quantities()
        totals = self.get_product_totals()
        
        results = []
        for i in range(min(len(prices), len(qtys), len(totals))):
            expected = prices[i] * qtys[i]
            actual = totals[i]
            results.append({
                'index': i,
                'price': prices[i],
                'quantity': qtys[i],
                'expected': expected,
                'actual': actual,
                'correct': abs(expected - actual) < 0.01
            })
        return results
    
    def unselect_all_items(self):
        checkboxes = self.find_elements(self.locators.ITEM_CHECKBOXES)
        for cb in checkboxes:
            try:
                if cb.is_selected():
                    self.execute_script("arguments[0].click();", cb)
                    time.sleep(0.5)
            except:
                pass
    
    def select_item_by_index(self, index):
        checkboxes = self.find_elements(self.locators.ITEM_CHECKBOXES)
        if index < len(checkboxes):
            try:
                if not checkboxes[index].is_selected():
                    self.execute_script("arguments[0].click();", checkboxes[index])
                    time.sleep(0.5)
                    return True
            except:
                pass
        return False
    
    def get_selected_items_count(self):
        text = self.get_text(self.locators.SELECTED_ITEMS)
        try:
            return int(text) if text else 0
        except:
            return 0
    
    def get_subtotal(self):
        text = self.get_text(self.locators.SUBTOTAL)
        try:
            return float(text) if text else 0.0
        except:
            return 0.0
    
    def get_grand_total(self):
        text = self.get_text(self.locators.GRAND_TOTAL)
        try:
            return float(text) if text else 0.0
        except:
            return 0.0
    
    def get_shipping_cost(self):
        text = self.get_text(self.locators.SHIPPING)
        try:
            return float(text.replace('₹', '')) if text else 50.0
        except:
            return 50.0
    
    def get_gst(self):
        text = self.get_text(self.locators.GST)
        try:
            return float(text.replace('₹', '')) if text else 50.0
        except:
            return 50.0
    
    def calculate_subtotal(self):
        total = 0.0
        items = self.find_elements(self.locators.CART_ITEMS)
        for item in items:
            try:
                checkbox = item.find_element(*self.locators.ITEM_CHECKBOXES)
                if checkbox.is_selected():
                    total_el = item.find_element(*self.locators.PRODUCT_TOTALS)
                    total += float(total_el.text)
            except:
                pass
        return total
    
    def calculate_grand_total(self):
        return self.calculate_subtotal() + self.get_shipping_cost() + self.get_gst()
    
    def is_checkout_button_displayed(self):
        btn = self.find_element(self.locators.CHECKOUT_BTN)
        return btn is not None and btn.is_displayed()
    
    def get_checkout_button_text(self):
        return self.get_text(self.locators.CHECKOUT_BTN)
    
    def click_checkout(self):
        return self.click(self.locators.CHECKOUT_BTN)