import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Ecommerce_automation.pages.cart_page import CartPage

def test_open_cart_and_remove_item(driver, base_url):
    wait = WebDriverWait(driver, 20)

    # Step 1: Open homepage
    driver.get(base_url)

    # Step 2: Click the shopping cart icon using JS click
    cart_icon = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-test='nav-cart']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cart_icon)
    driver.execute_script("arguments[0].click();", cart_icon)

    # Step 3: Wait for cart page container to load
    wait.until(EC.presence_of_element_located((By.XPATH, "//app-checkout[contains(@class,'ng-star-inserted')]")))

    # Step 4: Initialize CartPage object
    cart_page = CartPage(driver)

    # Step 5: Verify at least one item is in the cart
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "Cart is empty, nothing to remove"
    print("Number of items in cart before removal:", len(cart_items))

    # Step 6: Remove the first item
    cart_page.remove_first_item()

    # Step 7: Wait until the item is removed
    wait.until(lambda d: len(cart_page.get_cart_items()) == len(cart_items) - 1)

    # Step 8: Verify the item count decreased
    updated_cart_items = cart_page.get_cart_items()
    assert len(updated_cart_items) == len(cart_items) - 1, "Item was not removed from cart"
    print("Item removed successfully. Remaining items:", len(updated_cart_items))
