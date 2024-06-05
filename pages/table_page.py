import allure
from playwright.sync_api import expect
from config.errors import Errors
from config.links import Links
from data.table_page_data import TablePageLocators, TablePageData
from pages.base_page import BasePage


class TablePage(BasePage):
    locators = TablePageLocators()
    data = TablePageData()
    summ_all_price = 0
    PAGE_URL = Links.TABLE

    @allure.step('Получение суммы всех товаров из таблицы "Shopping List"')
    def get_summ_all_price(self):
        cells_table = self.page.locator(self.locators.CELLS_SHOPPING_LIST_TABLE).all()
        for i in range(len(cells_table)):
            if i % 2 == 0:
                continue
            else:
                self.summ_all_price += int(cells_table[i].text_content())
        return self.summ_all_price

    @allure.step('Проверка значения суммы в таблице')
    def expect_total_price(self):
        total = self.page.locator(self.locators.FOOTER_SHOPPING_LIST_TABLE).last
        assert self.get_summ_all_price() == int(total.text_content())

    @allure.step('Отметить чек-бокс в строке с именем Raj')
    def check_row_with_raj_name(self):
        rows = self.page.locator(self.locators.ROWS_TABLE_LETS_HANDLE_IT).all()
        for row in rows:
            if self.data.RAJ_NAME in row.all_inner_texts()[0].split('\t'):
                row.get_by_role('checkbox').check()

    def sort_column(self, column: str, direction: str):
        with allure.step(f'Отсортировать столбец {column} по направлению {direction}'):
            header = self.page.locator(self.locators.HEADERS_COLUMNS).filter(has_text=column)
            if direction == self.data.ASCENDING:
                while header.get_attribute(self.data.SORT_ATTRIBUTE) != self.data.ASCENDING:
                    header.click()
            elif direction == self.data.DESCENDING:
                while header.get_attribute(self.data.SORT_ATTRIBUTE) != self.data.DESCENDING:
                    header.click()

    def expect_sort_column(self, column: str, direction: str):
        with allure.step(f'Проверка сортировки стобца {column} в направлении {direction}'):
            index = 0
            match column:
                case self.data.DESSERT:
                    index = 0
                case self.data.CALORIES:
                    index = 1
                case self.data.FAT:
                    index = 2
                case self.data.CARBS:
                    index = 3
                case self.data.PROTEIN:
                    index = 4
                case self.data.CHOLESTEROL:
                    index = 5
            col = []
            rows = self.page.locator(self.locators.ROWS_SORT_TABLE).all()
            for row in rows:
                col.append(row.all_inner_texts()[0].split('\t\n')[index])
            if direction == self.data.ASCENDING:
                assert col == sorted(col), f'{Errors.SORT_ERROR} столбца {column}'
            elif direction == self.data.DESCENDING:
                assert col == sorted(col, reverse=True), f'{Errors.SORT_ERROR} столбца {column}'
