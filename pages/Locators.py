from dataclasses import dataclass

from playwright.sync_api import Page


@dataclass(frozen=True)
class Locators:
    input_username = lambda page: page.get_by_placeholder('Username')
    input_password = lambda page: page.locator('#password')

    @staticmethod
    def button_login(page):
        return page.locator('#login-button')

    @staticmethod
    def product_page_title(page):
        return page.locator("[data-test = 'title']")

    # Home Page
    @staticmethod
    def button_add_to_cart(page: Page):
        return page.locator('#add-to-cart-sauce-labs-bolt-t-shirt')

    @staticmethod
    def icon_shopping_cart_badge(page: Page):
        return page.locator('.shopping_cart_badge')