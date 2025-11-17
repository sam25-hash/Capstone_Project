import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

INVALID_USER = {
    "email": "invalid@example.com",
    "password": "wrongpassword"
}

def test_login_invalid(driver, base_url):
    """
    Test an invalid login on practicesoftwaretesting.com
    using invalid_user credentials.
    """
    driver.get(base_url + "/auth/login")
    wait = WebDriverWait(driver, 10)

    # Email input
    email = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-test='email']"))
    )
    email.send_keys(INVALID_USER["email"])

    # Password input
    password = driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
    password.send_keys(INVALID_USER["password"])

    # Login button
    login_btn = driver.find_element(By.CSS_SELECTOR, "input[data-test='login-submit']")
    login_btn.click()

    # Small sleep just to visually see the transition
    time.sleep(2)

    # Scroll down a bit to make sure the error is in view
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(1)

    # Wait for error message
    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".alert-danger, [data-test='login-error']")
        )
    )

    # Extra scroll into view for the error element itself
    driver.execute_script("arguments[0].scrollIntoView(true);", error)
    time.sleep(2)

    assert error.is_displayed()
    assert "Invalid email or password" in error.text
