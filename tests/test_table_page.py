import time

from pages.table_page import TablePage


class TestTablePage:
    def test_table_page_shopping_price(self, browser):
        table_page = TablePage(browser)
        table_page.navigate()
        table_page.expect_total_price()

    def test_table_page_lets_handle_it(self, browser):
        table_page = TablePage(browser)
        table_page.navigate()
        table_page.check_row_with_raj_name()
        time.sleep(3)