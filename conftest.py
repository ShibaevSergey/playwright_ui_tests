import pytest
from pages.querying_page import QueryingPage
from playwright.sync_api import Page


@pytest.fixture(scope='function')
def querying_page(page: Page):
    querying_page = QueryingPage(page)
    return querying_page