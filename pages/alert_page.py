import allure
from playwright.sync_api import expect
from config.links import Links
from data.alert_page_data import AlertPageLocators, AlertPageData
from pages.base_page import BasePage


class AlertPage(BasePage):
    locators = AlertPageLocators()
    data = AlertPageData()
    PAGE_URL = Links.ALERT

    @allure.step('Клик на кнопку "Simple Alert"')
    def click_btn_simple_alert(self):
        with allure.step('Ожидание простого Alert и его закрытие'):
            self.page.once('dialog', lambda dialog: dialog.accept())
        self.page.locator(self.locators.ACCEPT_BTN).click()

    @allure.step('Клик на кнопку "Confirm Alert"')
    def click_btn_confirm_alert(self):
        with allure.step('Ожидание и клик "Нет" в alert + текст уведомления'):
            def handle_dialog(dialog):
                print(dialog.message)
                allure.attach(dialog.message, 'Текст диалога', allure.attachment_type.TEXT)
                dialog.dismiss()

            self.page.once('dialog', handle_dialog)
        self.page.locator(self.locators.CONFIRM_BTN).click()

    @allure.step('Нажать на кнопку "Prompt Alert"')
    def click_btn_prompt_alert(self):
        with allure.step('Ожидание Prompt диалога и ввод имени'):
            self.page.once('dialog', lambda dialog: dialog.accept(self.data.NAME))
        self.page.locator(self.locators.PROMPT_BTN).click()

    @allure.step('Проверка введенного имени')
    def expect_entered_name(self):
        expect(self.page.locator(self.locators.MY_NAME)).to_contain_text(self.data.NAME)

    @allure.step('Клик на кнопку "Modern Alert"')
    def click_btn_modern_alert(self):
        self.page.locator(self.locators.MODERN_BTN).click()

    @allure.step('Проверка отображения модального окна')
    def expect_text_in_active_modern_alert(self):
        expect(self.page.locator(self.locators.ACTIVE_MODAL_ALERT)).to_contain_text(self.data.TEXT_MODERN_ALERT)

    @allure.step('Закрыть модальное окно "Modern Alert"')
    def close_modern_alert(self):
        self.page.locator(self.locators.CLOSE_ACTIVE_MODAL_ALERT_BTN).click()