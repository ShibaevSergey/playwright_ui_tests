from pages.radio_page import RadioPage


class TestRadioPage:
    def test_radio_page(self, browser):
        radio_page = RadioPage(browser)
        radio_page.navigate()
        radio_page.select_rb_yes_or_no()
        radio_page.search_bug()
        radio_page.expect_is_checked_only_one_rb()
        radio_page.search_checked_rb()
        radio_page.expect_disable_rb_maybe()
        radio_page.expect_cb_remember_me_is_checked()
        radio_page.check_cb_i_agree()
