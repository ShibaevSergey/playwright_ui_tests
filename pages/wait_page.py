import allure
from config.links import Links
from data.wait_page_data import WaitPageLocators
from pages.base_page import BasePage


class WaitPage(BasePage):
    locators = WaitPageLocators()
    PAGE_URL = Links.WAITS

    @allure.step('Ожидание и принятие Alert')
    def wait_and_accept_alert(self):
        with allure.step('Ожидание простого Alert и его закрытие'):
            self.page.once('dialog', lambda dialog: dialog.accept())
        with allure.step('Клик на кнопку "Accept"'):
            self.page.locator(self.locators.ACCEPT_BTN).click()
            self.page.wait_for_event('dialog', timeout=10000)
