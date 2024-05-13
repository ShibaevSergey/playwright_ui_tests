import time
import allure
from config.links import Links
from data.alert_page_data import AlertPageLocators
from pages.base_page import BasePage


class AlertPage(BasePage):
    locators = AlertPageLocators()
    PAGE_URL = Links.ALERT

    @allure.step('Клик на кнопку "Simple Alert"')
    def click_btn_simple_alert(self):
        self.page.locator(self.locators.ACCEPT_BTN).click()

    @allure.step('Закрыть простой alert')
    def accept_simple_alert(self):
        def accept_dialog(dialog):
            dialog.accept()
        self.page.on('dialog', accept_dialog)

    @allure.step('Клик на кнопку "Confirm Alert"')
    def click_btn_confirm_alert(self):
        self.page.locator(self.locators.CONFIRM_BTN).click()

    @allure.step('Нажать "Нет" в alert и получить текст уведомления')
    def dismiss_alert_and_print_message(self):
        def handle_dialog(dialog):
            print(dialog.message)
            time.sleep(3)
            allure.attach(dialog.message, 'Текст диалога', allure.attachment_type.TEXT)
            dialog.dismiss()

        self.page.on('dialog', handle_dialog)
