import pytest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def test_scroll_up_down_hover_down(driver, base_url):
    # Open homepage
    driver.get(base_url)
    time.sleep(2)  # wait for page to fully load

    # ------------------------
    # 1️⃣ Scroll to the top
    # ------------------------
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    # ------------------------
    # 2️⃣ Scroll down to middle/section
    # ------------------------
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
    time.sleep(1)

    # ------------------------
    # 3️⃣ Hover over a target element (example: "Contact" link)
    # ------------------------
    target_element = driver.find_element(By.LINK_TEXT, "Contact")  # Replace with desired element
    ActionChains(driver).move_to_element(target_element).perform()
    time.sleep(1)
    print("Hovered over element:", target_element.text)

    # ------------------------
    # 4️⃣ Scroll further down to the bottom
    # ------------------------
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
