import time

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
# user_data_dir = r"C:/Users/RITHEB/AppData/Local/Google/Chrome/User Data"  # Replace with your Chrome user data path
# browser = playwright.chromium.launch_persistent_context(user_data_dir, headless=False, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', args=["--start-maximized"])

page = browser.new_page()
page.set_default_timeout(60000)
# page.set_viewport_size({"width": 1920, "height": 1080})
page.goto("https://chatgpt.com/")
page.locator('//div[text()="Multiline Comments in Java"]').click()
page.locator('button[data-testid="close-sidebar-button"]').click()
# page.goto("https://chatgpt.com/c/67e52945-c9c4-8012-8f25-8bbf6010e8c2")
time.sleep(120)
