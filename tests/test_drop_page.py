from pages.drop_page import DropPage


class TestDropPage:
    def test_drop_page(self, browser):
        drop_page = DropPage(browser)
        drop_page.navigate()
        drop_page.expect_text_before_drag_and_drop()
        drop_page.drag_and_drop_first_box_to_second_box()
        drop_page.expect_text_after_drag_and_drop()
