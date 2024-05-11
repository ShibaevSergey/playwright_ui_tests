import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope='function')
def browser() -> Page:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(channel="chrome", headless=True)
    context = browser.new_context(ignore_https_errors=True, viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    yield page
    page.close()
    playwright.stop()
    