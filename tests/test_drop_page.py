from pages.drop_page import DropPage


class TestDropPage:
    def test_drop_page(self, browser):
        drop_page = DropPage(browser)
        drop_page.navigate()