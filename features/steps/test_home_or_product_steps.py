from behave import when, then
from pages.products_or_home_page import ProductsHomePage


@when(u'I clicked on the Add to cart button')
def step_impl(context):
    context.products_page: ProductsHomePage = ProductsHomePage(context.page)
    context.products_page.click_add_to_cart()



@then(u'I clicked on the Shopping cart badge icon')
def step_impl(context):
    context.products_page.click_badge_cart_icon()
