from behave import when, then
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@when(u'I clicked on the Checkout button')
def step_impl(context):
    context.cart_page: CartPage = CartPage(context.page)
    context.cart_page.click_checkout()


@then(u'\'Chekout: Your Information\' page is displayed')
def step_impl(context):
    context.checkout_page: CheckoutPage = CheckoutPage(context.page)
    context.checkout_page.validate_text_checkout_your_information()


@when(u'I enter \'First Name\' as "{first_name}"')
def step_impl(context, first_name):
    context.checkout_page.enter_first_name(first_name)


@when(u'I enter \'Last Name\' as "{last_name}"')
def step_impl(context, last_name):
    context.checkout_page.enter_last_name(last_name)


@when(u'I enter \'Zip Postal Code\' as "{zip_postal_code}"')
def step_impl(context, zip_postal_code):
    context.checkout_page.enter_zip_postal_code_name(zip_postal_code)


@when(u'I clicks \'Continue\' button')
def step_impl(context):
    context.checkout_page.click_button_continue()


@when(u'I clicks \'Finish\' button')
def step_impl(context):
    context.checkout_page.click_button_finish()


@then(u'\'Thank you for your order!\' message is displayed')
def step_impl(context):
    expect(context.checkout_page.validate_thank_you_message(), 'Thank you for your order!\' message is not displayed').to_be_visible()