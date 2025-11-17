from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    ADDRESS = (By.ID, "address")
    CITY = (By.ID, "city")
    CARD = (By.ID, "card")
    SUBMIT_BUTTON = (By.ID, "submitOrder")

    def fill_checkout_form(self, data):
        self.type(self.NAME, data["name"])
        self.type(self.EMAIL, data["email"])
        self.type(self.ADDRESS, data["address"])
        self.type(self.CITY, data["city"])
        self.type(self.CARD, data["card_no"])

    def place_order(self):
        self.click(self.SUBMIT_BUTTON)
