from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    PRODUCT_LIST = (By.CSS_SELECTOR, ".card")

    def get_products(self):
        return self.driver.find_elements(*self.PRODUCT_LIST)
