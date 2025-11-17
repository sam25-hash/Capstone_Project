import pytest
import allure
from pathlib import Path

# ----------------------------
# Correct imports for your structure
# ----------------------------
from Ecommerce_automation.utilities.driver_factory import create_driver
from Ecommerce_automation.utilities.config_reader import load_config
from Ecommerce_automation.utilities.logger import get_logger

logger = get_logger("conftest")

# ----------------------------
# Load config.yaml safely
# ----------------------------
CONFIG_PATH = Path(__file__).parent / "config" / "config.yaml"
CONFIG = load_config(CONFIG_PATH)  # This now always returns a dict

# ----------------------------
# Pytest command-line options
# ----------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=CONFIG["default_browser"],
        help="Browser to run tests: chrome, firefox, edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )

# ----------------------------
# Initialize WebDriver fixture
# ----------------------------
@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    logger.info(f"Launching browser: {browser} | headless={headless}")

    driver = create_driver(browser=browser, headless=headless)
    yield driver

    logger.info("Closing browser...")
    driver.quit()

# ----------------------------
# Base URL fixture
# ----------------------------
@pytest.fixture
def base_url():
    return CONFIG["base_url"]

# ----------------------------
# HomePage fixture (auto-load homepage)
# ----------------------------
@pytest.fixture
def home_page(driver, base_url):
    from Ecommerce_automation.pages.home_page import HomePage
    hp = HomePage(driver)
    hp.open(base_url)
    return hp

# ----------------------------
# Allure Screenshot on Failure
# ----------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                logger.error(f"Error capturing screenshot: {e}")
