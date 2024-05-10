import allure
from playwright.sync_api import expect

from config.links import Links
from data.input_page_data import InputPageLocators, InputPageData
from pages.base_page import BasePage


class InputPage(BasePage):
    locators = InputPageLocators()
    data = InputPageData()
    PAGE_URL = Links.INPUT

    @allure.step('Ввод полного имени')
    def input_full_name(self):
        self.page.locator(self.locators.FULL_NAME).fill(f'{self.data.FIRST_NAME} {self.data.LAST_NAME}')

    @allure.step('Дополнить текст в поле')
    def append_text(self):
        tbx = self.page.locator(self.locators.APPEND_TEXT)
        tbx.focus()
        tbx.press('End')
        tbx.type(f' {self.data.FIRST_NAME}')

    @allure.step('Нажать кнопку "Tab"')
    def press_tab(self):
        self.page.press(self.locators.APPEND_TEXT, 'Tab')

    @allure.step('Проверка текста в текстовом поле')
    def expect_text_in_text_box(self):
        expect(self.page.locator(self.locators.TEXT_BOX_FOR_GET_TEXT)).to_have_value(self.data.GETTING_TEXT)

    @allure.step('Очистка поля ввода')
    def clear_text_box(self):
        self.page.locator(self.locators.CLEAR_TBX).clear()

    @allure.step('Проверка того, что поле неактивно')
    def expect_text_box_disable(self):
        expect(self.page.locator(self.locators.DISABLE_TBX)).to_be_disabled()

    @allure.step('Проверка на наличие атрибута "readonly"')
    def expect_text_box_readonly(self):
        expect(self.page.locator(self.locators.DONT_WRITE)).to_have_attribute(self.data.READONLY, '')

    @allure.step('Попытка очистить поле "readonly"')
    def trying_clear_readonly_text_box(self):
        self.page.locator(self.locators.DONT_WRITE).clear(force=True)

    @allure.step('Проверка текста в поле "readonly"')
    def expect_text_in_readonly_text_box(self):
        expect(self.page.locator(self.locators.DONT_WRITE)).to_have_value(self.data.TEXT_READONLY)
