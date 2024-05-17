import random
import re
import allure
from playwright.sync_api import expect
from config.links import Links
from data.multiselect_page_data import MultiselectPageData
from pages.base_page import BasePage


class MultiselectPage(BasePage):
    data = MultiselectPageData()
    items = random.sample(data.ITEMS, 3)
    PAGE_URL = Links.MULTISELECT

    @allure.step('Выбрать три элемента')
    def select_multiple_item(self):
        self.page.keyboard.down('Control')
        try:
            for i in self.items:
                self.page.locator('div').filter(has_text=re.compile(i)).click()
        finally:
            self.page.keyboard.up('Control')

    @allure.step('Проверка того, что элементы отмечены')
    def expect_elements_is_selected(self):
        for i in self.items:
            expect(self.page.locator('div').filter(has_text=re.compile(i))).to_have_class(self.data.VALUE_ATTRIBUTE)
