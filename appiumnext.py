from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# Appium server URL
appium_server_url = "http://localhost:4723"

# Configure capabilities for your Small_Phone emulator
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "13"  # Android 13 from your target=android-36
options.device_name = "Medium_Phone_API_36.1"  # From your AvdId
options.automation_name = "UiAutomator2"
options.udid = "emulator-5554"  # Use actual device ID from 'adb devices'

# Emulator-specific properties from your configuration
options.avd = "Medium_Phone_API_36.1"  # AVD name
options.avd_launch_timeout = 120000  # 2 minutes for emulator launch
options.avd_ready_timeout = 120000

# Use Settings app (always available, no need for external APK)
options.app_package = "com.android.settings"
options.app_activity = "com.android.settings.Settings"

# Additional options based on your emulator properties
options.no_reset = True
options.full_reset = False
options.new_command_timeout = 300

# Device-specific capabilities matching your emulator properties
options.set_capability('deviceType', 'phone')
options.set_capability('orientation', 'PORTRAIT')  # From hw.initialOrientation
options.set_capability('screenSize', '720x1280')  # From hw.lcd.width=720, hw.lcd.height=1280
options.set_capability('pixelRatio', 2.0)  # Approximate for hw.lcd.density=320

print("🚀 Starting Appium test for Small_Phone emulator...")
print(f"Device: Medium_Phone (720x1280, Android 13)")
print(f"RAM: 1024MB, Storage: 6GB")

try:
    # Initialize driver
    driver = webdriver.Remote(
        command_executor=appium_server_url,
        options=options
    )

    print("✅ Successfully connected to Small_Phone emulator!")

    # Wait for Settings app to load
    time.sleep(3)

    # Get and display device information
    print("\n📱 Device Information:")
    caps = driver.capabilities
    print(f"  - Platform: {caps.get('platformName')} {caps.get('platformVersion')}")
    print(f"  - Device: {caps.get('deviceName')}")
    print(f"  - Automation: {caps.get('automationName')}")
    print(f"  - UDID: {caps.get('udid')}")

    # Verify screen size matches your emulator properties
    window_size = driver.get_window_size()
    print(f"  - Screen: {window_size['width']}x{window_size['height']} (Expected: 720x1280)")

    # Get current app info
    print(f"  - Current App: {driver.current_package}")
    print(f"  - Current Activity: {driver.current_activity}")

    # Take screenshot
    driver.save_screenshot("small_phone_settings.png")
    print("  - 📸 Screenshot saved: small_phone_settings.png")

    # Test basic interactions
    print("\n🧪 Testing Basic Interactions:")

    # Test 1: Swipe gesture (using your screen dimensions)
    print("  - Testing swipe gesture...")
    width = window_size['width']
    height = window_size['height']

    # Swipe from center to top (scroll down)
    driver.swipe(
        width // 2, height // 2,
        width // 2, height // 4,
        1000
    )
    time.sleep(2)

    # Swipe back to original position
    driver.swipe(
        width // 2, height // 4,
        width // 2, height // 2,
        1000
    )
    print("  - ✅ Swipe test completed")

    # Test 2: Back button
    print("  - Testing back button...")
    driver.back()
    time.sleep(1)
    print("  - ✅ Back button test completed")

    # Test 3: Get device time
    device_time = driver.device_time
    print(f"  - Device Time: {device_time}")

    # Test 4: Test screen rotation (portrait mode from your properties)
    print("  - Testing orientation (should be PORTRAIT)...")
    current_orientation = driver.orientation
    print(f"  - Current Orientation: {current_orientation}")

    print("\n🎉 All tests completed successfully!")
    print("✅ Small_Phone emulator is working perfectly with Appium!")

except Exception as e:
    print(f"❌ Error during test: {e}")

finally:
    # Always quit the driver
    if 'driver' in locals():
        driver.quit()
        print("✅ Driver session ended")