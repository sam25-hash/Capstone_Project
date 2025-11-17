from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KeywordEngine:
    def __init__(self, driver):
        self.driver = driver
        self.locator_map = {
            "id": By.ID,
            "name": By.NAME,
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "link": By.LINK_TEXT
        }

    def openURL(self, url):
        self.driver.get(url)

    def click(self, by, value):
        locator = (self.locator_map[by], value)
        self.driver.find_element(*locator).click()

    def type(self, by, value, text):
        locator = (self.locator_map[by], value)
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(text)

    def verifyText(self, by, value, expected):
        locator = (self.locator_map[by], value)
        actual = self.driver.find_element(*locator).text
        assert expected in actual, f"Expected {expected}, got {actual}"
