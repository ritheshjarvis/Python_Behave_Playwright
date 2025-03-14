from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.text_checkout_your_information = page.get_by_text('Checkout: Your Information')
        self.input_first_name = page.locator('#first-name')
        self.input_last_name = page.locator('#last-name')
        self.input_zip_postal_code_name = page.locator('#postal-code')
        self.button_continue = page.locator('#continue')
        self.button_finish = page.locator('#finish')
        self.text_thank_you_message = page.locator('.complete-header')
        self.button_back_home = page.locator('#back-to-products')

    def validate_text_checkout_your_information(self):
        return self.button_back_home

    def enter_first_name(self, first_name):
        self.input_first_name.fill(first_name)

    def enter_last_name(self, last_name):
        self.input_last_name.fill(last_name)

    def enter_zip_postal_code_name(self, zip_postal_code):
        self.input_zip_postal_code_name.fill(zip_postal_code)

    def click_button_continue(self):
        self.button_continue.click()

    def click_button_finish(self):
        self.button_finish.click()

    def click_button_back_home(self):
        self.button_back_home.click()

    def validate_thank_you_message(self):
        return self.text_thank_you_message