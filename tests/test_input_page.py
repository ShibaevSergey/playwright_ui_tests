import time
from pages.input_page import InputPage


class TestInputPage:
    def test_input(self, browser):
        input_page = InputPage(browser)
        input_page.navigate()
        input_page.input_full_name()
        input_page.append_text()
        input_page.press_tab()
        input_page.expect_text_in_text_box()
        input_page.clear_text_box()
        input_page.expect_text_box_disable()
        input_page.expect_text_box_readonly()
        input_page.trying_clear_readonly_text_box()
        input_page.expect_text_in_readonly_text_box()
