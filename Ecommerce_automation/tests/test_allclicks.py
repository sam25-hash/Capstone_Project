import pytest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_all_clicks(driver, base_url):
    wait = WebDriverWait(driver, 10)

    # Open homepage
    driver.get(base_url)
    time.sleep(2)  # wait for page to fully load

    # ------------------------
    # 1️⃣ Normal click on first product card
    # ------------------------
    first_product = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.row.ng-star-inserted"))
    )
    first_product.click()
    time.sleep(1)
    print("Normal click on first product done.")

    # ------------------------
    # 2️⃣ JS click on "Add to cart" button
    # ------------------------
    add_to_cart_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-test='add-to-cart']"))
    )
    driver.execute_script("arguments[0].click();", add_to_cart_btn)
    time.sleep(1)
    print("JS click on Add to Cart button done.")

    # ------------------------
    # 3️⃣ Double-click on the first product again (for demo)
    # ------------------------
    first_product = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.row.ng-star-inserted"))
    )
    ActionChains(driver).double_click(first_product).perform()
    time.sleep(1)
    print("Double-click on first product done.")

    # ------------------------
    # 4️⃣ Right-click (context click) on the first product
    # ------------------------
    first_product = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.row.ng-star-inserted"))
    )
    ActionChains(driver).context_click(first_product).perform()
    time.sleep(1)
    print("Right-click on first product done.")
