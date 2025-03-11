from playwright.sync_api import Page

from pages.Locators import Locators
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def click_add_to_cart(self):
        Locators.button_add_to_cart(self.page).click()

    def click_badge_cart_icon(self):
        Locators.icon_shopping_cart_badge(self.page).click()