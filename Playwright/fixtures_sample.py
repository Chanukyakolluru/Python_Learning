from playwright.sync_api import Page

def test_fixture(page: Page):
    page.goto('https://sports.ladbrokes.com')


