from pages.Locators import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def enter_username_password(self, username, password):
        Locators.input_username(self.page).fill(username)
        Locators.input_password(self.page).fill(password)

    def click_login_button(self):
        Locators.button_login(self.page).click()
