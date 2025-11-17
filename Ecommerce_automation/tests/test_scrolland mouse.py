import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    yield drv
    drv.quit()

def test_scroll_and_hover(driver):
    driver.get("https://practicesoftwaretesting.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    # Smooth scroll down
    total_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(0, total_height, 200):  # scroll in steps of 200px
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(0.3)  # small delay for visible scrolling

    time.sleep(1)  # pause at bottom

    # Smooth scroll up
    for i in range(total_height, 0, -200):
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(0.3)

    time.sleep(1)  # pause at top

    # Hover over nav items and show dropdowns
    nav_xpaths = [
        "//a[contains(text(),'Home')]",
        "//a[contains(text(),'Contact')]",
        "//a[contains(text(),'Categories')]",
        "//a[contains(text(),'Sign in')]"
    ]

    for xpath in nav_xpaths:
        nav_elem = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        actions.move_to_element(nav_elem).perform()
        print("Hovered over:", nav_elem.text)
        time.sleep(1.5)  # wait to see the hover effect

        # If nav has a dropdown, hover over the dropdown items too
        try:
            dropdown_items = nav_elem.find_elements(By.XPATH, ".//following-sibling::ul//a")
            for item in dropdown_items:
                actions.move_to_element(item).perform()
                print("Hovered over dropdown:", item.text)
                time.sleep(1)  # delay to see dropdown hover
        except:
            pass
