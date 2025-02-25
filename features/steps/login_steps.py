import time

from playwright.sync_api import sync_playwright
from behave import given, when, then
from pages.login_page import LoginPage

@given('I am on the login page')
def step_open_login_page(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto("https://www.saucedemo.com/")



@when('I enter "{username}" as username and "{password}" as password')
def step_enter_credentials(context, username, password):
    context.login_page = LoginPage(context.page)
    context.login_page.login(username, password)

    time.sleep(10)
    pass
    # context.login_page.login(username, password)

@when('I click the login button')
def step_click_login_button(context):
    pass  # Login action is already performed in the previous step

@then('I should see the dashboard')
def step_verify_dashboard(context):
    pass
    # assert "Dashboard" in context.page.title()
    # context.browser.close()
    # context.playwright.stop()