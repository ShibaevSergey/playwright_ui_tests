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

    @allure.step('Получить список локаторов кнопок страниц')
    def get_locators_page_buttons(self):
        btns = []
        buttons = self.page.locator(self.locators.PAGE_BUTTONS).all()
        for btn in buttons:
            class_attribute = btn.get_attribute(self.data.CLASS)
            if self.data.CLASS_CURRENT_PAGE != class_attribute:
                btns.append(btn)
        return btns

    @allure.step('Перейти на случайную страницу из доступных и проверить корректность перехода')
    def go_to_random_page(self):
        buttons = self.get_locators_page_buttons()
        if len(buttons) != 0:
            btn_number = random.randint(0, len(buttons)-1)
            print(btn_number)
            buttons[btn_number].click()
            self.pause(300)
            expect(buttons[btn_number]).to_have_class(self.data.CLASS_CURRENT_PAGE)

    @allure.step('Получить номер текущей страницы')
    def get_number_current_page(self):
        buttons = self.page.locator(self.locators.PAGE_BUTTONS).all()
        count = 0
        for btn in buttons:
            class_attribute = btn.get_attribute(self.data.CLASS)
            if self.data.CLASS_CURRENT_PAGE == class_attribute:
                count = int(btn.text_content())
                break
        return count

    @allure.step('Нажать на кнопку "Next"')
    def click_btn_next(self):
        self.page.locator(self.locators.NEXT_BTN).click()

    @allure.step('Проверка работы кнопки "Next"')
    def expect_next_button(self):
        before = self.get_number_current_page()
        self.click_btn_next()
        after = self.get_number_current_page()
        assert (before + 1) == after

    @allure.step('Нажать на кнопку "Last"')
    def click_btn_last(self):
        self.page.locator(self.locators.LAST_BTN).click()

    @allure.step('Нажать на кнопку "First"')
    def click_btn_first(self):
        self.page.locator(self.locators.FIRST_BTN).click()

    @allure.step('Нажать на кнопку "Previous"')
    def click_btn_previous(self):
        self.page.locator(self.locators.PREVIOUS_BTN).click()

    @allure.step('Проверка работы кнопки "Last"')
    def expect_last_button(self):
        buttons = self.get_locators_page_buttons()
        number_last_page = ''
        if len(buttons) != 0:
            number_last_page = buttons[-1].text_content()
        self.click_btn_last()
        number_current_page = self.get_number_current_page()
        assert int(number_last_page) == number_current_page

    @allure.step('Проверка работы кнопки "Previous"')
    def expect_previous_button(self):
        self.click_btn_last()
        before = self.get_number_current_page()
        self.click_btn_previous()
        after = self.get_number_current_page()
        assert (before - 1) == after

    @allure.step('Проверка работы кнопки "First"')
    def expect_first_button(self):
        self.click_btn_last()
        self.click_btn_first()
        assert self.get_number_current_page() == 1

    def sort_column(self, column: str, direction: str):
        with allure.step(f'Отсортировать столбец {column} по направлению {direction}'):
            header = self.page.get_by_label(column)
            if direction == self.data.ASCENDING:
                while header.get_attribute(self.data.SORT_ATTRIBUTE) != self.data.ASCENDING:
                    header.click()
            elif direction == self.data.DESCENDING:
                while header.get_attribute(self.data.SORT_ATTRIBUTE) != self.data.DESCENDING:
                    header.click()

    def expect_sort_column(self, column: str, direction: str):
        with allure.step(f'Проверка сортировки стобца {column} в направлении {direction}'):
            index: int = 0
            match column:
                case self.data.S_NO:
                    index = 0
                case self.data.UNIVERSITY_NAME:
                    index = 1
                case self.data.COUNTRY:
                    index = 2
                case self.data.WEBSITE:
                    index = 3
            col = []
            rows = self.page.locator(self.locators.ROWS_TABLE).all()
            for row in rows:
                inner_text = row.all_inner_texts()
                split_inner_text = inner_text[0].split('\t')
                col.append(split_inner_text[index])
            if direction == self.data.ASCENDING:
                sort_col = sorted(col)
                assert sort_col == col
            elif direction == self.data.DESCENDING:
                reverse_sort_col = sorted(col, reverse=True)
                assert reverse_sort_col == col
