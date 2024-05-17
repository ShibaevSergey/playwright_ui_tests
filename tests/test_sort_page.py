import time

from pages.sort_page import SortPage
from data.sort_page_data import SortPageData


class TestSortPage:
    def test_sort_page(self, browser):
        sort_page = SortPage(browser)
        sort_page.navigate()
        sort_page.move_element_to_done(SortPageData.GET_TO_WORK)
        sort_page.move_element_to_done(SortPageData.PICK_UP_GROCERIES)
        sort_page.move_element_to_done(SortPageData.GO_HOME)
        sort_page.move_element_to_done(SortPageData.FALL_ASLEEP)
        sort_page.move_element_to_do(SortPageData.CHECK_EMAIL)
        sort_page.move_element_to_do(SortPageData.TAKE_A_SHOWER)
        sort_page.move_drag_above_drop(SortPageData.WALK_DOG, SortPageData.TAKE_A_SHOWER)
        sort_page.move_drag_under_drop(SortPageData.CHECK_EMAIL, SortPageData.BRUSH_TEETH)