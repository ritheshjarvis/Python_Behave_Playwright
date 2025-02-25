import time

# from pages.Locators import Locators
from pages.LocatorsClass import Locators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):
        # self.page.locator(Locators.input_username).fill(username)
        # self.page.get_by_placeholder('Username').fill(username)
        Locators.input_username(self.page).fill(username)
        # # self.page.fill(Locators.input_username, username)
        # # time.sleep(5)
        Locators.input_password(self.page).fill(password)
        # # self.page.fill(Locators.input_password, password)
        # self.page.click(Locators.button_login)
        Locators.button_login(self.page).click()