import time
from data.table_page_data import TablePageData
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

    def test_table_page_sortable_dessert(self, browser):
        table_page = TablePage(browser)
        table_page.navigate()
        table_page.sort_column(TablePageData.DESSERT, TablePageData.DESCENDING)
        table_page.expect_sort_column(TablePageData.DESSERT, TablePageData.DESCENDING)
        table_page.sort_column(TablePageData.DESSERT, TablePageData.ASCENDING)
        table_page.expect_sort_column(TablePageData.DESSERT, TablePageData.ASCENDING)

    def test_table_page_sortable_calories(self, browser):
        table_page = TablePage(browser)
        table_page.navigate()
        table_page.sort_column(TablePageData.CALORIES, TablePageData.DESCENDING)
        table_page.expect_sort_column(TablePageData.CALORIES, TablePageData.DESCENDING)
        table_page.sort_column(TablePageData.CALORIES, TablePageData.ASCENDING)
        table_page.expect_sort_column(TablePageData.CALORIES, TablePageData.ASCENDING)

    def test_table_page_sortable_fat(self, browser):
        table_page = TablePage(browser)
        table_page.navigate()
        table_page.sort_column(TablePageData.FAT, TablePageData.DESCENDING)
        table_page.expect_sort_column(TablePageData.FAT, TablePageData.DESCENDING)
        table_page.sort_column(TablePageData.FAT, TablePageData.ASCENDING)
        table_page.expect_sort_column(TablePageData.FAT, TablePageData.ASCENDING)

    def test_table_page_sortable_carbs(self, browser):
        table_page = TablePage(browser)
        table_page.navigate()
        table_page.sort_column(TablePageData.CARBS, TablePageData.DESCENDING)
        table_page.expect_sort_column(TablePageData.CARBS, TablePageData.DESCENDING)
        table_page.sort_column(TablePageData.CARBS, TablePageData.ASCENDING)
        table_page.expect_sort_column(TablePageData.CARBS, TablePageData.ASCENDING)

    def test_table_page_sortable_protein(self, browser):
        table_page = TablePage(browser)
        table_page.navigate()
        table_page.sort_column(TablePageData.PROTEIN, TablePageData.DESCENDING)
        table_page.expect_sort_column(TablePageData.PROTEIN, TablePageData.DESCENDING)
        table_page.sort_column(TablePageData.PROTEIN, TablePageData.ASCENDING)
        table_page.expect_sort_column(TablePageData.PROTEIN, TablePageData.ASCENDING)

    def test_table_page_sortable_cholesterol(self, browser):
        table_page = TablePage(browser)
        table_page.navigate()
        table_page.sort_column(TablePageData.CHOLESTEROL, TablePageData.DESCENDING)
        table_page.expect_sort_column(TablePageData.CHOLESTEROL, TablePageData.DESCENDING)
        table_page.sort_column(TablePageData.CHOLESTEROL, TablePageData.ASCENDING)
        table_page.expect_sort_column(TablePageData.CHOLESTEROL, TablePageData.ASCENDING)
