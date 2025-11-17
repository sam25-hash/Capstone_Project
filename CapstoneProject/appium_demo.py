from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time
import subprocess
import os


class MobileTest:
    def __init__(self):
        self.driver = None

    def setup_android_environment(self):
        """Set up Android environment variables for current session"""
        print("🔧 Setting up Android environment...")

        android_sdk_path = "C:\\Users\\samiksha.devan\\AppData\\Local\\Android\\Sdk"

        # Set environment variables for this session
        os.environ['ANDROID_HOME'] = android_sdk_path
        os.environ['ANDROID_SDK_ROOT'] = android_sdk_path

        # Add to PATH for this session
        platform_tools = f"{android_sdk_path}\\platform-tools"
        tools = f"{android_sdk_path}\\tools"
        build_tools = f"{android_sdk_path}\\build-tools"

        current_path = os.environ.get('PATH', '')
        new_paths = f"{platform_tools};{tools};{build_tools}"

        if new_paths not in current_path:
            os.environ['PATH'] = f"{new_paths};{current_path}"

        print(f"✅ ANDROID_HOME set to: {android_sdk_path}")
        return True

    def check_adb_connection(self):
        """Check if ADB can connect to the device"""
        print("📱 Checking ADB connection...")

        try:
            result = subprocess.run(
                ['adb', 'devices'],
                capture_output=True,
                text=True,
                timeout=10
            )

            if 'emulator-5554' in result.stdout and 'device' in result.stdout:
                print("✅ ADB connected to emulator-5554")
                return True
            else:
                print("❌ ADB cannot find emulator-5554")
                print(f"ADB output: {result.stdout}")
                return False

        except Exception as e:
            print(f"❌ ADB check failed: {e}")
            return False

    def start_driver_simple(self):
        """Start Appium driver with minimal capabilities"""
        print("🚀 Starting Appium driver...")

        # Setup environment first
        self.setup_android_environment()

        appium_server_url = "http://localhost:4723"

        # Minimal capabilities - let Appium auto-detect
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"

        # Use the specific device ID from adb
        options.udid = "emulator-5554"

   # Optional: Use Settings app for testing
        options.app_package = "com.android.settings"
        options.app_activity = "com.android.settings.Settings"

        # Timeout settings
        options.new_command_timeout = 60

        try:
            print("Connecting to Appium server...")
            self.driver = webdriver.Remote(
                command_executor=appium_server_url,
                options=options
            )

            self.driver.implicitly_wait(10)
            print("✅ Appium driver started successfully!")
            return True

        except Exception as e:
            print(f"❌ Failed to start driver: {e}")
            return False

    def test_basic_functionality(self):
        """tests basic Appium functionality"""
        print("\n🧪 Testing Basic Functionality")

        try:
            # Get device capabilities
            caps = self.driver.capabilities
            print(f"   Platform: {caps.get('platformName')}")
            print(f"   Version: {caps.get('platformVersion')}")
            print(f"   Device: {caps.get('deviceName')}")
            print(f"   UDID: {caps.get('udid')}")

            # tests screen interaction
            window_size = self.driver.get_window_size()
            print(f"   Screen size: {window_size['width']}x{window_size['height']}")

            # tests taking screenshot
            self.driver.save_screenshot("basic_test.png")
            print("   📸 Screenshot saved: basic_test.png")

            return True

        except Exception as e:
            print(f"   ❌ Basic functionality test failed: {e}")
            return False

    def test_settings_app(self):
        """tests interacting with Settings app"""
        print("\n⚙️ Testing Settings App")

        try:
            # Wait for Settings to load
            time.sleep(3)

            # Get current app info
            current_package = self.driver.current_package
            current_activity = self.driver.current_activity
            print(f"   Current app: {current_package}")
            print(f"   Current activity: {current_activity}")

            # Try to find available options
            elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
            visible_options = []

            for element in elements:
                try:
                    text = element.text
                    if text and text.strip():
                        visible_options.append(text.strip())
                except:
                    continue

            print(f"   Found {len(visible_options)} text elements")

            # Show first 5 options
            if visible_options:
                print("   First 5 options:")
                for option in visible_options[:5]:
                    print(f"     - {option}")

            # tests back button
            self.driver.back()
            time.sleep(2)

            return True

        except Exception as e:
            print(f"   ⚠️ Settings app test issue: {e}")
            return False

    def test_swipe_gesture(self):
        """tests swipe gesture"""
        print("\n🔄 Testing Swipe Gesture")

        try:
            size = self.driver.get_window_size()

            # Swipe down
            self.driver.swipe(
                size['width'] // 2, size['height'] * 0.7,
                size['width'] // 2, size['height'] * 0.3,
                1000
            )
            print("   ✅ Swipe down completed")

            time.sleep(1)

            # Swipe up
            self.driver.swipe(
                size['width'] // 2, size['height'] * 0.3,
                size['width'] // 2, size['height'] * 0.7,
                1000
            )
            print("   ✅ Swipe up completed")

            return True

        except Exception as e:
            print(f"   ❌ Swipe test failed: {e}")
            return False

    def stop_driver(self):
        """Stop the Appium driver"""
        if self.driver:
            self.driver.quit()
            print("✅ Driver stopped successfully")


def main():
    """Main test execution"""
    print("=" * 60)
    print("🤖 APPIUM AUTOMATION TEST (No Admin Rights Required)")
    print("=" * 60)

    # Create test instance
    test = MobileTest()

    # Check ADB connection first
    if not test.check_adb_connection():
        print("\n❌ Please make sure:")
        print("   1. Android emulator is running")
        print("   2. You can see 'emulator-5554 device' in 'adb devices'")
        return

    try:
        # Start driver
        if not test.start_driver_simple():
            print("\n💡 Troubleshooting tips:")
            print("   1. Make sure Appium server is running: appium --port 4723")
            print("   2. Try restarting the emulator")
            print("   3. Check if port 4723 is available")
            return

        # Run tests
        tests = [
            test.test_basic_functionality,
            test.test_settings_app,
            test.test_swipe_gesture
        ]

        passed = 0
        total = len(tests)

        print("\n" + "=" * 40)
        print("🏃 RUNNING TESTS")
        print("=" * 40)

        for test_func in tests:
            if test_func():
                passed += 1
            print()  # Empty line between tests

        # Print summary
        print("=" * 40)
        print("📊 TEST SUMMARY")
        print("=" * 40)
        print(f"Tests passed: {passed}/{total}")

        if passed == total:
            print("🎉 All tests passed successfully!")
        elif passed > 0:
            print("⚠️ Some tests passed - basic functionality is working!")
        else:
            print("❌ No tests passed - need to troubleshoot")

    except Exception as e:
        print(f"💥 tests execution failed: {e}")
    finally:
        test.stop_driver()


if __name__ == "__main__":
    main()