from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    for items in [p.chromium,p.firefox,p.webkit]:
        browser =items.launch()
        page = browser.new_page()
        page.goto('https://google.com')
        page.screenshot(path =f'example-{items.name}.png')
        browser.close()