import allure
import random
from playwright.sync_api import expect
from config.links import Links
from data.select_page_data import SelectPageLocators, SelectPageData
from pages.base_page import BasePage

class SelectPage(BasePage):
    locators = SelectPageLocators()
    data = SelectPageData()
    PAGE_URL = Links.SELECT

    @allure.step('Выбор яблока из выпадающего списка "Фрукты"')
    def select_apple_from_fruits(self):
        self.page.locator(self.locators.SELECT_FRUITS).select_option(self.data.APPLE)

    @allure.step('Выбор нескольких супергероев из списка')
    def select_superheros_from_list(self):
        self.page.locator(self.locators.MULTISELECT_SUPERHEROS).select_option(
            random.sample(self.data.SUPERHEROS, 3))

    @allure.step('Выбор языка программирования')
    def select_programming_language(self):
        self.page.locator(self.locators.SELECT_LANG).select_option(index=4)

    @allure.step('Напечатать все элементы выпадающего списка (язык программирования)')
    def print_all_programming_language(self):
        list = self.page.locator(self.locators.SELECT_LANG).inner_text()
        # print(list[0].strip())
        allure.attach(str(list), 'Список языков программирования', allure.attachment_type.TEXT)

    @allure.step('Выбор страны из списка по значению (value)')
    def select_india_country(self):
        self.page.locator(self.locators.SELECT_COUNTRY).select_option(value=self.data.INDIA_VALUE)

    @allure.step('Проверка выбранной страны')
    def expect_select_country(self):
        expect(self.page.locator(self.locators.SELECT_COUNTRY)).to_have_value(self.data.INDIA_VALUE)