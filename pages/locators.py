from dataclasses import dataclass

from playwright.sync_api import Page


@dataclass(frozen=True)
class Locators:
    input_username = lambda page: page.get_by_placeholder('Username')
    input_password = lambda page: page.locator('#password')

    @staticmethod
    def button_login(page):
        return page.locator('#login-button')

    # Products or Home Page
    @staticmethod
    def product_page_title(page):
        return page.locator("[data-test = 'title']")

    @staticmethod
    def button_add_to_cart(page: Page):
        return page.locator('#add-to-cart-sauce-labs-bolt-t-shirt')

    @staticmethod
    def icon_shopping_cart_badge(page: Page):
        return page.locator('.shopping_cart_badge')

    # cart page
    @staticmethod
    def button_checkout(page: Page):
        return page.locator('#checkout')

    # checkout page
    @staticmethod
    def input_first_name(page: Page):
        return page.locator('#first-name')

    @staticmethod
    def input_last_name(page: Page):
        return page.locator('#last-name')

    @staticmethod
    def input_zip_postal_code_name(page: Page):
        return page.locator('#postal-code')

    @staticmethod
    def button_continue(page: Page):
        return page.locator('#continue')

    @staticmethod
    def button_finish(page: Page):
        return page.locator('#finish')

    @staticmethod
    def text_thank_you_message(page: Page):
        return page.locator('.complete-header')

    @staticmethod
    def button_back_home(page: Page):
        return page.locator('#back-to-products')
