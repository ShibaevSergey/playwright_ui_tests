import time

from pages.alert_page import AlertPage


class TestAlertPage:
    def test_alert_page(self, browser):
        alert_page = AlertPage(browser)
        alert_page.navigate()
        # alert_page.click_btn_simple_alert()
        # alert_page.accept_simple_alert()
        # alert_page.click_btn_confirm_alert()
        alert_page.dismiss_alert_and_print_message()