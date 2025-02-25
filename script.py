from playwright.sync_api import Page, sync_playwright

p = sync_playwright().start()  # Start Playwright

browser = p.chromium.launch(headless=True)  # Set headless=False to see the browser
page = browser.new_page()
page.goto("https://www.hyrtutorials.com/p/waits-demo.html")
page.fill()
page.click()
page.get
page.screenshot(path="screenshot.png")  # Save screenshot
print(page.title())  # Print page title
browser.close()
