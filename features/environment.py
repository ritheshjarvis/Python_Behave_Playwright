import os
import time

from playwright.sync_api import sync_playwright

def before_all(context):
    browser_name = os.getenv("BROWSER", context.config.userdata.get("browser", "chromium"))
    print("----------------> {browser_name}")
    context.playwright = sync_playwright().start()
    if browser_name == "firefox":
        context.browser = context.playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        context.browser = context.playwright.webkit.launch(headless=False)
    else:
        context.browser = context.playwright.chromium.launch(headless=False)

def before_scenario(context, scenario):
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()

def after_scenario(context, scenario):
    time.sleep(5)
    context.page.close()
    context.browser_context.close()


def after_all(context):
    context.browser.close()
    context.playwright.stop()
