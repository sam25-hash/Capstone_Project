import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_add_to_cart_scroll(driver, base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver, 20)
    time.sleep(1)

    # Step 1: Enter search term
    search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='search-query']")))
    search_input.clear()
    search_input.send_keys("hammer")
    time.sleep(0.5)

    # Step 2: Click search button
    search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='search-submit']")))
    driver.execute_script("arguments[0].scrollIntoView();", search_btn)
    time.sleep(0.5)
    search_btn.click()
    time.sleep(2)  # wait for results to load

    # Step 3: Click the first product (<a> with class 'card')
    first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'card')])[1]")))
    driver.execute_script("arguments[0].scrollIntoView();", first_product)
    time.sleep(0.5)
    first_product.click()
    time.sleep(2)  # wait for product page

    # Step 4: Scroll to Add to Cart button and click
    add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_btn)  # scroll so button is centered
    time.sleep(0.5)
    add_to_cart_btn.click()
    time.sleep(2)  # wait for cart update

    print("Product added to cart successfully")
