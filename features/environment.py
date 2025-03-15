import base64
import os
import time

from playwright.sync_api import sync_playwright

from utils.Reporters import Reporters


def before_all(context):
    browser_name = os.getenv("BROWSER", context.config.userdata.get("browser", "chromium"))
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
    context.page.close()
    context.browser_context.close()

def after_step(context, step):
    if step.status == 'failed':
        screenshot_data = context.page.screenshot()
        screenshot_data_base64 = base64.b64encode(screenshot_data).decode()
        reporters = Reporters(context)
        reporters.add_screenshot_to_HTMLFormatter(screenshot_data_base64, "Step Screenshot")

def after_all(context):
    context.browser.close()
    context.playwright.stop()
