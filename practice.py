import time


from playwright.sync_api import sync_playwright, expect

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
context = browser.new_context()
page = context.new_page()

expect.set_options(timeout=8000) # 5s by default
page.set_default_timeout(5000) # 30s by default
page.set_default_navigation_timeout(1000) # 30s by default
page.goto("https://www.saucedemo.com/") # get

page.locator('#user-name').fill('standard_user') # send_keys
class_name = page.locator('#password').get_attribute('class') # get_attribute
print(class_name)
page.locator('#login-button').click()
expect(page.locator('.title1'), 'Sorry. Not visible... ' ).to_be_visible() # assertion
page.wait_for_selector('', state='')

# print("We filled the Locator")
# time.sleep(5)
