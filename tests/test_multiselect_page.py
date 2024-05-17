from pages.multiselect_page import MultiselectPage


class TestMultiselectPage:
    def test_multiselect_page(self, browser):
        multiselect_page = MultiselectPage(browser)
        multiselect_page.navigate()
        multiselect_page.select_multiple_item()
        multiselect_page.expect_elements_is_selected()
