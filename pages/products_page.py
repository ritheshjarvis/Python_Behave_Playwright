from pages.Locators import Locators
from pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def validate_product_page(self):
        return Locators.product_page_title(self.page)