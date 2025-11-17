from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage(BasePage):
    # Correct locator for first product card
    FIRST_PRODUCT_CARD = (By.CSS_SELECTOR, "div.row.ng-star-inserted")

    # Add to cart button
    ADD_TO_CART = (By.CSS_SELECTOR, "button[data-test='add-to-cart']")

    def click_first_product(self):
        """Click on the first product card"""
        element = self.find(self.FIRST_PRODUCT_CARD)
        element.click()

    def js_click_add_to_cart(self):
        """Click Add to Cart using JavaScript"""
        element = self.find(self.ADD_TO_CART)
        self.driver.execute_script("arguments[0].click();", element)

    def double_click_first_product(self):
        """Double-click on the first product card"""
        element = self.find(self.FIRST_PRODUCT_CARD)
        ActionChains(self.driver).double_click(element).perform()

    def right_click_first_product(self):
        """Right-click (context click) on the first product card"""
        element = self.find(self.FIRST_PRODUCT_CARD)
        ActionChains(self.driver).context_click(element).perform()

    def hover_over_first_product(self):
        """Hover over the first product card"""
        element = self.find(self.FIRST_PRODUCT_CARD)
        ActionChains(self.driver).move_to_element(element).perform()
