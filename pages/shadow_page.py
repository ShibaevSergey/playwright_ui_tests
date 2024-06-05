import allure
from config.links import Links
from data.shadow_page_data import ShadowPageLocators, ShadowPageData
from pages.base_page import BasePage


class ShadowPage(BasePage):
    locators = ShadowPageLocators()
    data = ShadowPageData()
    PAGE_URL = Links.SHADOW

    @allure.step('Ввод имени')
    def input_first_name(self):
        self.page.locator(self.locators.FIRST_NAME).fill(self.data.FIRST_NAME)

    @allure.step('Ввод фамилии')
    def input_last_name(self):
        self.page.locator(self.locators.FIRST_NAME).focus()
        self.page.keyboard.press('Tab')
        self.page.locator(self.locators.LAST_NAME).type(self.data.LAST_NAME)

    @allure.step('Ввод email')
    def input_email(self):
        self.page.locator(self.locators.FIRST_NAME).focus()
        self.page.keyboard.press('Tab')
        self.page.keyboard.press('Tab')
        self.page.locator(self.locators.EMAIL).type(self.data.EMAIL)
