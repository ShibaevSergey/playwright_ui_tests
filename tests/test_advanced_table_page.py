from data.advanced_table_page_data import AdvancedTablePageData
from pages.advanced_table_page import AdvancedTablePage


class TestAdvancedTablePage:
    def test_advanced_table_page_search(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.fill_search_request()
        advanced_table_page.expect_search_results()

    def test_advanced_table_page_count_row(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.expect_count_rows(AdvancedTablePageData.COUNT_10)
        advanced_table_page.expect_count_rows(AdvancedTablePageData.COUNT_5)
        advanced_table_page.expect_count_rows(AdvancedTablePageData.COUNT_25)

    def test_advanced_table_page_switch_page(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.go_to_random_page()

    def test_advanced_table_page_btn_next(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.expect_next_button()
        advanced_table_page.expect_next_button()

    def test_advanced_table_page_btn_last(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.expect_last_button()

    def test_advanced_table_page_btn_previous(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.expect_previous_button()

    def test_advanced_table_page_btn_first(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.expect_first_button()

    def test_advanced_table_page_btn_sort_s_no(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.sort_column(AdvancedTablePageData.S_NO, AdvancedTablePageData.DESCENDING)
        advanced_table_page.expect_sort_column(AdvancedTablePageData.S_NO, AdvancedTablePageData.DESCENDING)
        advanced_table_page.sort_column(AdvancedTablePageData.S_NO, AdvancedTablePageData.ASCENDING)
        advanced_table_page.expect_sort_column(AdvancedTablePageData.S_NO, AdvancedTablePageData.ASCENDING)

    def test_advanced_table_page_btn_sort_university(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.sort_column(AdvancedTablePageData.UNIVERSITY_NAME, AdvancedTablePageData.DESCENDING)
        advanced_table_page.expect_sort_column(AdvancedTablePageData.UNIVERSITY_NAME, AdvancedTablePageData.DESCENDING)
        advanced_table_page.sort_column(AdvancedTablePageData.UNIVERSITY_NAME, AdvancedTablePageData.ASCENDING)
        advanced_table_page.expect_sort_column(AdvancedTablePageData.UNIVERSITY_NAME, AdvancedTablePageData.ASCENDING)

    def test_advanced_table_page_btn_sort_country(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.sort_column(AdvancedTablePageData.COUNTRY, AdvancedTablePageData.DESCENDING)
        advanced_table_page.expect_sort_column(AdvancedTablePageData.COUNTRY, AdvancedTablePageData.DESCENDING)
        advanced_table_page.sort_column(AdvancedTablePageData.COUNTRY, AdvancedTablePageData.ASCENDING)
        advanced_table_page.expect_sort_column(AdvancedTablePageData.COUNTRY, AdvancedTablePageData.ASCENDING)

    def test_advanced_table_page_btn_sort_website(self, browser):
        advanced_table_page = AdvancedTablePage(browser)
        advanced_table_page.navigate()
        advanced_table_page.sort_column(AdvancedTablePageData.WEBSITE, AdvancedTablePageData.DESCENDING)
        advanced_table_page.expect_sort_column(AdvancedTablePageData.WEBSITE, AdvancedTablePageData.DESCENDING)
        advanced_table_page.sort_column(AdvancedTablePageData.WEBSITE, AdvancedTablePageData.ASCENDING)
        advanced_table_page.expect_sort_column(AdvancedTablePageData.WEBSITE, AdvancedTablePageData.ASCENDING)
