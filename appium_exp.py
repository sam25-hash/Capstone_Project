from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import time

print("🚀 Starting Appium Test (No TouchAction)")

# ------------------------------------
# APPIUM OPTIONS (Appium 3.x)
# ------------------------------------
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Medium_Phone"
options.automation_name = "UiAutomator2"
options.no_reset = True

# Enable automatic chromedriver download
options.set_capability("appium:chromedriver_autodownload", True)
options.set_capability(
    "appium:chromedriverExecutableDir",
    "C:\\Users\\samiksha.devan\\chromedrivers"
)
options.set_capability("appium:ensureWebviewsHavePages", True)

# Launch Chrome browser
options.app_package = "com.android.chrome"
options.app_activity = "com.google.android.apps.chrome.Main"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(5)

# ------------------------------------
# 1️⃣ OPEN WEBSITE
# ------------------------------------
url = "https://rahulshettyacademy.com/AutomationPractice/"
print("🌐 Opening:", url)

driver.get(url)
time.sleep(5)

# ------------------------------------
# 2️⃣ CLICK OPERATION
# ------------------------------------
try:
    home_btn = driver.find_element(AppiumBy.ID, "home-btn")
    home_btn.click()
    print("✔ Click successful")
except:
    print("⚠ Home button not found, skipping")

driver.back()
time.sleep(3)

# ------------------------------------
# 3️⃣ SEND KEYS OPERATION
# ------------------------------------
try:
    name_input = driver.find_element(AppiumBy.ID, "name")
    name_input.send_keys("Saranya Testing Appium")
    print("✔ send_keys successful")
except:
    print("❌ send_keys failed")

time.sleep(3)

# ------------------------------------
# 4️⃣ DRAG AND DROP USING W3C ACTIONS
# ------------------------------------
print("🎯 Performing W3C Drag & Drop...")

try:
    source = driver.find_element(AppiumBy.ID, "draggable")
    target = driver.find_element(AppiumBy.ID, "droppable")

    actions = ActionChains(driver)
    finger = PointerInput(PointerInput.INTERACTION_TOUCH, "finger")
    action_builder = ActionBuilder(driver, mouse=finger)

    # Drag and drop with W3C actions
    action_builder.pointer_action.move_to(source).pause(0.2)
    action_builder.pointer_action.pointer_down()
    action_builder.pointer_action.move_to(target).pause(0.2)
    action_builder.pointer_action.pointer_up()

    action_builder.perform()

    print("✔ Drag & Drop successful")
except Exception as e:
    print("❌ Drag & Drop failed:", e)

time.sleep(3)

# ------------------------------------
# END TEST
# ------------------------------------
driver.quit()
print("✅ Test Completed Without TouchAction")
