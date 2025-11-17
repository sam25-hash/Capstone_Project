from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[@id='search-query']")       # updated
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='search-submit']")  # updated
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    PRODUCTS_LINK = (By.LINK_TEXT, "Products")

    def search_product(self, term):
        self.type(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)

    def go_to_login(self):
        self.click(self.LOGIN_LINK)

    def go_to_products(self):
        self.click(self.PRODUCTS_LINK)
