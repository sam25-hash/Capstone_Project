import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


def test_select_hand_tools_children_only(driver):
    driver.get("https://practicesoftwaretesting.com/")
    wait = WebDriverWait(driver, 20)

    # Scroll a bit so left filter panel is visible
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(1)

    # 1) Locate the "By category:" heading
    by_category = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h4[normalize-space()='By category:']")
        )
    )
    print("Found 'By category:' heading")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", by_category)
    time.sleep(1)

    # 2) Find the fieldset that belongs to By category
    categories_fieldset = by_category.find_element(
        By.XPATH, "following-sibling::fieldset[1]"
    )
    print("Found categories fieldset")

    # DEBUG: print all top-level category labels under this fieldset
    top_level_labels = categories_fieldset.find_elements(By.XPATH, ".//div[contains(@class,'checkbox')]/label")
    print("Top level category labels under 'By category:' fieldset:")
    for lbl in top_level_labels:
        print("  ->", lbl.text)

    # 3) Find the HAND TOOLS parent block by its label text
    hand_tools_block = categories_fieldset.find_element(
        By.XPATH, ".//div[contains(@class,'checkbox')][.//label[contains(normalize-space(),'Hand Tools')]]"
    )
    print("Found Hand Tools block")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hand_tools_block)
    time.sleep(1)

    # NOTE: We intentionally DO NOT click the parent Hand Tools checkbox.

    # 4) Now select only Hammer, Hand Saw, Wrench, Pliers
    target_subcategories = ["Hammer", "Hand Saw", "Wrench", "Pliers"]

    for tool_name in target_subcategories:
        # child checkbox is inside the ul > fieldset within hand_tools_block
        sub_xpath = (
            ".//ul//fieldset//div[contains(@class,'checkbox')][.//label[contains(normalize-space(),'"
            + tool_name +
            "')]]//input[@type='checkbox']"
        )
        print(f"Looking for checkbox of: {tool_name}")
        sub_checkbox = hand_tools_block.find_element(By.XPATH, sub_xpath)

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_checkbox)
        time.sleep(0.5)

        if not sub_checkbox.is_selected():
            sub_checkbox.click()
            print(f"Clicked checkbox: {tool_name}")
            time.sleep(1)

        assert sub_checkbox.is_selected(), f"{tool_name} checkbox was not selected"

    print("All required Hand Tools children selected successfully.")
    time.sleep(3)
