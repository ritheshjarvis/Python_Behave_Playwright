from dataclasses import dataclass


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