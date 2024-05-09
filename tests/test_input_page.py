import time
from pages.input_page import InputPage


class TestInputPage:
    def test_input_full_name(self, browser):
        input_page = InputPage(browser)
        input_page.navigate()
        input_page.input_full_name()


    def test_append_text(self, browser):
        input_page = InputPage(browser)
        input_page.navigate()
        input_page.append_text()
        input_page.press_tab()
