import allure
from playwright.sync_api import expect
from config.links import Links
from data.windows_page_data import WindowsPageLocators, WindowsPageData
from pages.base_page import BasePage


class WindowsPage(BasePage):
    locators = WindowsPageLocators()
    data = WindowsPageData()
    PAGE_URL = Links.WINDOWS

    @allure.step('Клик на кнопку "Open Home Page"')
    def click_btn_open_home_page(self):
        self.page.locator(self.locators.BTN_OPEN_HOME_PAGE).click()

    @allure.step('Ожидание открытия новой вкладки при клике на кнопку')
    def wait_new_tab(self, context):
        with context.expect_page() as event_info:
            self.click_btn_open_home_page()
            return event_info.value

    @allure.step('Клик на кнопку "Multiple Windows"')
    def click_btn_multiple_windows(self):
        self.page.locator(self.locators.BTN_MULTIPLE_WINDOWS).click()
        self.page.wait_for_timeout(500)

    @allure.step('Проверка адресов открытых вкладок')
    def expect_url_open_tabs(self, context):
        list_tabs = context.pages
        for i in range(len(list_tabs)):
            expect(list_tabs[i]).to_have_url(self.data.LIST_URLS[i])

    @allure.step('Закрытие всех вкладок')
    def close_all_tabs(self, context):
        list_tabs = context.pages
        for i in list_tabs:
            i.close()

