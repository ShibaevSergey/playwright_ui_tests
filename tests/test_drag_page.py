from pages.drag_page import DragPage


class TestDragPage:
    def test_drag_page(self, browser):
        drag_page = DragPage(browser)
        drag_page.navigate()
        drag_page.drag_and_drop_box()
        drag_page.expect_dragged_box()
