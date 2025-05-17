from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=2000)
    page = browser.new_page()
    page.goto('https://sports.ladbrokes.com')
    browser.close()

