from pages.base_page import BasePage
from pages.locators import Locators


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.button_checkout = page.locator('#checkout')

    def click_checkout(self):
        self.button_checkout.click()

