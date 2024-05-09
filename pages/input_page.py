import allure
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