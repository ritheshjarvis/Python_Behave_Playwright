import time

from playwright.sync_api import sync_playwright, expect
from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_or_home_page import ProductsHomePage


@given('I am on the login page')
def step_open_login_page(context):
    expect.set_options(timeout=8000)
    context.page.goto("https://www.saucedemo.com/")


@when('I enter "{username}" as username and "{password}" as password')
def step_enter_credentials(context, username, password):
    context.login_page = LoginPage(context.page)
    context.login_page.enter_username_password(username, password)

@when('I click the login button')
def step_click_login_button(context):
    context.login_page.click_login_button()


@then('I should see the product home page')
def step_verify_dashboard(context):
    context.products_page = ProductsHomePage(context.page)
    expect(context.products_page.validate_product_page(), 'Product title not visible').to_be_visible()
