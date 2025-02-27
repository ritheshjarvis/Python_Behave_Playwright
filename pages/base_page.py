from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(20000)

    def navigate(self, url):
        self.page.goto(url)
