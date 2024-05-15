from pages.frame_page import FramePage

class TestFramePage:
    def test_frame_page(self, browser):
        frame_page = FramePage(browser)
        frame_page.navigate()
        frame_page.input_first_name_in_frame()
        frame_page.input_last_name_in_frame()
        frame_page.input_email_in_inner_frame()