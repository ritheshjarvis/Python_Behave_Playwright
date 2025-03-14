from pages.base_page import BasePage


class ProductsHomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.product_page_title = page.locator("[data-test = 'title']")
        self.button_add_to_cart = page.locator('#add-to-cart-sauce-labs-bolt-t-shirt')
        self.icon_shopping_cart_badge = page.locator('.shopping_cart_badge')

    def validate_product_page(self):
        return self.product_page_title

    def click_add_to_cart(self):
        self.button_add_to_cart.click()

    def click_badge_cart_icon(self):
        self.icon_shopping_cart_badge.click()