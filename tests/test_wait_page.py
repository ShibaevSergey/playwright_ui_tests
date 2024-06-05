from pages.wait_page import WaitPage


class TestWaitPage:
    def test_wait_page(self, browser):
        wait_page = WaitPage(browser)
        wait_page.navigate()
        wait_page.wait_and_accept_alert()