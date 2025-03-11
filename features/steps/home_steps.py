from behave import when, then

from pages.home_page import HomePage


@when(u'I clicked on the Add to cart button')
def step_impl(context):
    context.home_page: HomePage = HomePage(context.page)
    context.home_page.click_add_to_cart()



@then(u'I clicked on the Shopping cart badge icon')
def step_impl(context):
    context.home_page.click_badge_cart_icon()
