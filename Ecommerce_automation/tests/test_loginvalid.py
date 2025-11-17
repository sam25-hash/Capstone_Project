import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_valid(driver, base_url):
    """
    Test a valid login on practicesoftwaretesting.com
    """
    driver.get(base_url + "/auth/login")
    wait = WebDriverWait(driver, 10)

    # Email input
    email = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-test='email']"))
    )
    email.send_keys("customer@practicesoftwaretesting.com")

    # Password input
    password = driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
    password.send_keys("welcome01")

    # Login button
    login_btn = driver.find_element(By.CSS_SELECTOR, "input[data-test='login-submit']")
    login_btn.click()

    # Optional: Assert login succeeded by checking for a known element on dashboard
    # Example (adjust as needed):
    # dashboard_element = wait.until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, "div.dashboard"))
    # )
    # assert dashboard_element.is_displayed()

