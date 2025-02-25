from dataclasses import dataclass


@dataclass(frozen=True)
class Locators:
    input_username = lambda page: page.get_by_placeholder('Username') # pylint: disable=unnecessary-lambda
    input_password = lambda page: page.locator('#password')
    # button_login = lambda page: page.locator('#login-button')

    @staticmethod
    def button_login(page):
        return page.locator('#login-button')