import allure
from config.links import Links
from data.querying_page_data import QueryingPageLocators, QueryingPageData
from pages.base_page import BasePage
from playwright.sync_api import Page, expect



class QueryingPage(BasePage):
    locators = QueryingPageLocators()
    data = QueryingPageData()
    PAGE_URL = Links.QUERYING

    @allure.step(f'Клик на кнопку {data.BTN_NAME}')
    def click_btn(self):
        self.page.locator(self.locators.BTN).click()

    @allure.step('Проверка имени кнопки')
    def expect_btn_name(self):
        expect(self.page.locator(self.locators.BTN)).to_have_text(self.data.BTN_NAME)

