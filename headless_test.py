from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Configuration
base_url = "https://practicesoftwaretesting.com/"
default_browser = "chrome"

print(f"Starting headless Selenium test on {base_url} using {default_browser}...")

# Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open the base URL
    driver.get(base_url)
    print("Page title:", driver.title)

    # Example: Extract the first <h1> text
    header = driver.find_element(By.TAG_NAME, "h1")
    print("Header text:", header.text)

finally:
    driver.quit()
    print("Headless Selenium test finished.")
