import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def smooth_click(driver, element, after=1.2):
    """Scroll element into view and click with JS, then wait a bit."""
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.8)  # small pause to see scroll
    driver.execute_script("arguments[0].click();", element)
    time.sleep(after)  # pause to observe UI change

def test_cart_flow(driver, base_url):
    wait = WebDriverWait(driver, 15)

    # 1️⃣ Open homepage
    driver.get(base_url)
    time.sleep(3)  # observe homepage

    # 2️⃣ Open "Categories" dropdown
    categories = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='nav-categories']"))
    )
    smooth_click(driver, categories, after=1.5)
    print("Clicked Categories")

    # 3️⃣ Click "Power Tools"
    power_tools = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='nav-power-tools']"))
    )
    smooth_click(driver, power_tools, after=2)
    print("Clicked Power Tools")

    # Small scroll to adjust view
    driver.execute_script("window.scrollBy(0, 350);")
    time.sleep(1.2)
    driver.execute_script("window.scrollBy(0, -150);")
    time.sleep(1.2)

    # 4️⃣ Open "Sheet Sander" product
    sheet_sander = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h5[@data-test='product-name' and normalize-space()='Sheet Sander']")
        )
    )
    smooth_click(driver, sheet_sander, after=2)
    print("Opened Sheet Sander product")

    # 5️⃣ Click "Add to cart" 3 times
    add_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='add-to-cart']"))
    )

    for i in range(3):
        smooth_click(driver, add_btn, after=1.3)
        print(f"Clicked Add to cart {i+1} time(s)")

        # After 3rd click → immediately go to cart
        if i == 2:
            cart_icon = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='nav-cart']"))
            )
            smooth_click(driver, cart_icon, after=2.5)
            print("Clicked cart icon (top-right)")

    # 6️⃣ Wait for Cart page step label just to be sure page loaded (no assert)
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'label')][normalize-space()='Cart']")
        )
    )
    print("Cart page visible")

    # Final scroll to see cart contents
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(3)  # keep page visible before test ends

