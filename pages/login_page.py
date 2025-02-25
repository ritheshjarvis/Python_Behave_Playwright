import time

from pages.Locators import Locators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):
        # self.page.locator(Locators.input_username).fill(username)
        self.page.get_by_placeholder('Username').fill(username)
        time.sleep(5)
        self.page.fill(Locators.input_password, password)
        self.page.click(Locators.button_login)