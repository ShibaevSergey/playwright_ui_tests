import allure
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