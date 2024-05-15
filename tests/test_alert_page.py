from pages.alert_page import AlertPage


class TestAlertPage:
    def test_alert_page(self, browser):
        alert_page = AlertPage(browser)
        alert_page.navigate()
        alert_page.click_btn_simple_alert()
        alert_page.click_btn_confirm_alert()
        alert_page.click_btn_prompt_alert()
        alert_page.expect_entered_name()
        alert_page.click_btn_modern_alert()
        alert_page.expect_text_in_active_modern_alert()
        alert_page.close_modern_alert()
