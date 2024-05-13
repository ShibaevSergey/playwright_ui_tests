from pages.select_page import SelectPage


class TestSelectPage:
    def test_select_page(self, browser):
        select_page = SelectPage(browser)
        select_page.navigate()
        select_page.select_apple_from_fruits()
        select_page.select_superheros_from_list()
        select_page.select_programming_language()
        select_page.print_all_programming_language()
        select_page.select_india_country()
        select_page.expect_select_country()