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
        self.page.locator(self.locators.BUTTON_BTN).click()

    @allure.step('Проверка имени кнопки')
    def expect_btn_name(self):
        expect(self.page.locator(self.locators.BUTTON_BTN)).to_have_text(self.data.BTN_NAME)

    @allure.step('Проверка класса в блоке DIV с data-test-id')
    def get_class_from_data_test_id(self):
        expect(self.page.locator(self.locators.DIV_WITH_DATA_TEST_ID)).to_have_class(self.data.CLASS_DIV_WITH_DATA_TEST_ID)

    @allure.step('Проверка классов с выбором элемента по тексту')
    def expect_class_elements_from_text(self):
        expect(self.page.get_by_text(self.data.APPLES, exact=True)).to_have_class(self.data.APPLES_CLASS)
        expect(self.page.get_by_text(self.data.ORANGES, exact=True)).to_have_class(self.data.ORANGES_CLASS)
        expect(self.page.get_by_text(self.data.BANANAS, exact=True)).to_have_class(self.data.BANANAS_CLASS)
        expect(self.page.get_by_text(self.data.MORE_APPLES, exact=True)).to_have_class(self.data.MORE_APPLES_CLASS)

    @allure.step('Проверка класса с выбором элемента по роли')
    def expect_class_element_from_role(self):
        expect(self.page.get_by_role('button', name=self.data.BTN_SAVE_FROM_NAME)).to_have_class(self.data.BTN_SAVE_FROM_NAME_CLASS)

    @allure.step('Ввод имени')
    def input_name(self):
        self.page.locator(self.locators.INPUT_NAME).fill(self.data.FILL_NAME)

    @allure.step('Ввод почты и поиск элемента по цепочке')
    def input_email(self):
        self.page.locator(self.locators.QUERY_FORM).locator(self.locators.INPUT_EMAIL).fill(self.data.EMAIL)

    @allure.step('Ввод пароля и поиск элемента (последний из списка)')
    def input_password(self):
        password_input = self.page.locator('input').last
        password_input.scroll_into_view_if_needed()
        password_input.fill(self.data.PASSWORD)

    @allure.step('Клик на кнопку "Submit"')
    def click_btn_submit(self):
        self.page.locator(self.locators.SUBMIT_BTN).click()