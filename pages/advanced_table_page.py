import random

import allure
from playwright.sync_api import expect
from config.links import Links
from data.advanced_table_page_data import AdvancedTablePageLocators, AdvancedTablePageData
from pages.base_page import BasePage


class AdvancedTablePage(BasePage):
    locators = AdvancedTablePageLocators()
    data = AdvancedTablePageData()
    PAGE_URL = Links.ADVANCED_TABLE
    searchRequest = data.SEARCH_PATTERN[random.randint(0, len(data.SEARCH_PATTERN) - 1)]

    def fill_search_request(self):
        with allure.step(f'Ввод поискового запроса: {self.searchRequest}'):
            self.page.locator(self.locators.INPUT_SEARCH).fill(self.searchRequest)
            self.pause(500)

    @allure.step('Проверка результатов поиска')
    def expect_search_results(self):
        def assert_search_row_numbers(arr):
            with allure.step('Проверка номеров найденных строк'):
                rows = self.page.locator(self.locators.ROWS_TABLE).all()
                for i in range(len(arr)):
                    assert rows[i].all_inner_texts()[0].split('\t')[0] == str(arr[i])
        if self.searchRequest == self.data.SEARCH_PATTERN[0]:
            assert_search_row_numbers(self.data.AMERICAN_NO)
        elif self.searchRequest == self.data.SEARCH_PATTERN[1]:
            assert_search_row_numbers(self.data.EDU_NO)
        elif self.searchRequest == self.data.SEARCH_PATTERN[2]:
            self.choose_count_rows_per_page(self.data.COUNT_25)
            assert_search_row_numbers(self.data.LONDON_NO)
        elif self.searchRequest == self.data.SEARCH_PATTERN[3]:
            assert_search_row_numbers(self.data.NO_35)

    @allure.step('Выбрать количество отображаемых строк таблицы на странице')
    def choose_count_rows_per_page(self, count: str):
        self.page.locator(self.locators.SELECT_COUNT_ROWS).select_option(count)

    @allure.step('Проверка количества отображаемых в таблице строк')
    def expect_count_rows(self, count: str):
        self.choose_count_rows_per_page(count)
        rows = self.page.locator(self.locators.ROWS_TABLE).all()
        assert str(len(rows)) == count


