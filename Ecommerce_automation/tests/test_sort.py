import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_sort_a_to_z_and_price_to_195():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        wait = WebDriverWait(driver, 15)

        # 1) Open homepage
        driver.get("https://practicesoftwaretesting.com/")
        time.sleep(2)

        # 2) Scroll down to show filters
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)

        # 3) Filters container
        filters = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-test='filters']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", filters)
        time.sleep(2)

        # 4) Sort: Name (A - Z)
        sort_dropdown = filters.find_element(By.CSS_SELECTOR, "select[data-test='sort']")
        Select(sort_dropdown).select_by_value("name,asc")
        time.sleep(2)

        # 5) Slider / max handle
        slider = filters.find_element(By.CSS_SELECTOR, "ngx-slider")
        max_handle = slider.find_element(By.CSS_SELECTOR, ".ngx-slider-pointer-max")
        track = slider.find_element(By.CSS_SELECTOR, ".ngx-slider-full-bar")

        min_value = 0
        max_value = 200
        target_value = 195

        driver.execute_script("arguments[0].scrollIntoView(true);", slider)
        time.sleep(2)

        # Get track rect
        track_rect = driver.execute_script(
            """
            const rect = arguments[0].getBoundingClientRect();
            return {left: rect.left, width: rect.width, top: rect.top, height: rect.height};
            """,
            track,
        )
        track_left = track_rect["left"]
        track_width = track_rect["width"]

        # Get handle rect
        handle_rect = driver.execute_script(
            """
            const rect = arguments[0].getBoundingClientRect();
            return {left: rect.left, width: rect.width, top: rect.top, height: rect.height};
            """,
            max_handle,
        )
        handle_center_x = handle_rect["left"] + handle_rect["width"] / 2

        # Calculate pixel position for target 195 on track
        value_range = max_value - min_value
        pixels_per_unit = track_width / value_range
        target_x = track_left + (target_value - min_value) * pixels_per_unit

        # How many pixels to move from current handle center to target position
        move_x = target_x - handle_center_x

        print(f"Track left: {track_left}, width: {track_width}")
        print(f"Handle center x: {handle_center_x}")
        print(f"Target x for 195: {target_x}")
        print(f"Move_x (pixels): {move_x}")

        actions = ActionChains(driver)

        # Drag max handle from its center by the exact delta
        actions.click_and_hold(max_handle).move_by_offset(move_x, 0).release().perform()
        time.sleep(2)

        final_value = int(max_handle.get_attribute("aria-valuenow"))
        print(f"Final max handle value after drag: {final_value}")

        # Optional: keep view nice
        driver.execute_script("window.scrollBy(0, -150);")
        time.sleep(3)

    finally:
        driver.quit()
