from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    # Locator for all cart items
    CART_ITEMS = (By.CSS_SELECTOR, "div.cart-item")  # Each product in cart

    # Locator for remove button of the first item
    REMOVE_BUTTON = (By.XPATH, "(//a[contains(@class,'btn btn-danger')])[1]")

    # Locator for checkout button (optional)
    CHECKOUT_BUTTON = (By.XPATH, "//button[@data-test='proceed-1']")

    def get_cart_items(self):
        """
        Returns a list of WebElement objects representing items in the cart
        """
        return self.driver.find_elements(*self.CART_ITEMS)

    def remove_first_item(self):
        """
        Removes the first item from the cart
        """
        self.click(self.REMOVE_BUTTON)

    def proceed_to_checkout(self):
        """
        Clicks the checkout button
        """
        self.click(self.CHECKOUT_BUTTON)
