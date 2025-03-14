from pages.locators import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.input_username = page.get_by_placeholder('Username')
        self.input_password = page.locator('#password')
        self.button_login = page.locator('#login-button')

    def enter_username_password(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)

    def click_login_button(self):
        self.button_login.click()