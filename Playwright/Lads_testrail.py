import asyncio
from playwright.async_api import async_playwright

async def run():
    # Replace these with your TestRail credentials and URL
    testrail_url = "https://ladbrokescoral.testrail.com/index.php?/runs/view/231472"
    username = "chanukya.kolluru@ivycomptech.com"
    password = "Chani@1986"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set headless=True to run without UI
        context = await browser.new_context()
        page = await context.new_page()

        # Step 1: Go to the login page
        await page.goto(testrail_url)

        # Step 2: Fill in credentials and log in
        await page.fill("input#name", username)
        await page.fill("input#password", password)
        await page.click("button#button_primary")

        # Step 3: Wait for navigation and dashboard load
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(5000)  # wait 5 seconds for dashboard to load fully

        # Step 4: Take a screenshot
        await page.screenshot(path="testrail_dashboard.png", full_page=False)
        print("Screenshot saved as 'testrail_dashboard.png'.")

        # Cleanup
        await browser.close()

# Run the Playwright script
asyncio.run(run())