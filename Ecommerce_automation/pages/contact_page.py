import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class ContactPage(BasePage):
    # Form fields
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    EMAIL = (By.ID, "email")
    SUBJECT = (By.ID, "subject")
    MESSAGE = (By.ID, "message")
    ATTACHMENT = (By.ID, "attachment")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-test='contact-submit']")
    SUCCESS_TEXT = (By.CSS_SELECTOR, "div.alert.alert-success.mt-3")  # precise locator

    def open(self, base_url):
        """Open contact page directly via URL"""
        self.driver.get(base_url + "/contact")

    def fill_form(self, first_name, last_name, email, message, subject=None, attachment_path=None):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.EMAIL, email)
        self.type(self.MESSAGE, message)

        if subject:
            select = Select(self.find(self.SUBJECT))
            select.select_by_visible_text(subject)

        if attachment_path:
            # Wait for input to be visible and send file
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ATTACHMENT)
            )
            element.send_keys(attachment_path)

    def submit_form(self, delay_after_click=3):
        element = self.find(self.SUBMIT_BUTTON)
        # Scroll into view and click
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        # Wait some seconds to visually see the result
        time.sleep(delay_after_click)

    def is_successful(self):
        try:
            # Wait for the success message to appear
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUCCESS_TEXT)
            )
            return True
        except:
            return False
