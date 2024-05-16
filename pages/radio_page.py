import random
import allure
from playwright.sync_api import expect
from config.links import Links
from data.radio_page_data import RadioPageLocators, RadioPageData
from pages.base_page import BasePage


class RadioPage(BasePage):
    locators = RadioPageLocators()
    data = RadioPageData()
    PAGE_URL = Links.RADIO

    @allure.step('Отметить один из RadioButton "Yes" или "No"')
    def select_rb_yes_or_no(self):
        yes_and_no_rb_locators = [self.locators.RB_YES_ANY, self.locators.RB_NO_ANY]
        self.page.locator(yes_and_no_rb_locators[random.randint(0, 1)]).check()

    @allure.step('Проверка что можно выбрать только один "Radio Button"')
    def expect_is_checked_only_one_rb(self):
        rb_yes_one = self.page.locator(self.locators.RB_YES_ONE)
        rb_no_one = self.page.locator(self.locators.RB_NO_ONE)
        rb_yes_one.check()
        expect(rb_yes_one).to_be_checked()
        expect(rb_no_one).not_to_be_checked()
        rb_no_one.check()
        expect(rb_yes_one).not_to_be_checked()
        expect(rb_no_one).to_be_checked()

    @allure.step('Поиск бага')
    def search_bug(self):
        rb_yes_bug = self.page.locator(self.locators.RB_YES_BUG)
        rb_no_bug = self.page.locator(self.locators.RB_NO_BUG)
        rb_yes_bug.check()
        expect(rb_yes_bug).to_be_checked()
        expect(rb_no_bug).not_to_be_checked()
        rb_no_bug.check()
        if rb_yes_bug.is_checked() and rb_no_bug.is_checked():
            print('Bug found, Radio Button "Yes" and Radio Button "No" is checked')
            allure.attach('Bug found, Radio Button "Yes" and Radio Button "No" is checked',
                          'Bug description', allure.attachment_type.TEXT)

    @allure.step('Поиск отмеченного Radio Button')
    def search_checked_rb(self):
        foo_rb = self.page.locator(self.locators.FOO_RB)
        bar_rb = self.page.locator(self.locators.BAR_RB)
        radio_buttons = [foo_rb, bar_rb]
        for i in radio_buttons:
            if i.is_checked():
                print(f'{i.get_attribute("id")} is checked')
                allure.attach(f'{i.get_attribute("id")} is checked', 'Выбранный Radio Button', allure.attachment_type.TEXT)

    @allure.step('Проверка что Radio Button "Maybe" не активен')
    def expect_disable_rb_maybe(self):
        expect(self.page.locator(self.locators.MAYBE_RB)).to_be_disabled()

    @allure.step('Проверка что чек-бокс "Remember me" отмечен')
    def expect_cb_remember_me_is_checked(self):
        expect(self.page.get_by_label(self.data.CB_REMEMBER_ME_LABEL)).to_be_checked()

    @allure.step('Отметить чек-бокс "I agree"')
    def check_cb_i_agree(self):
        self.page.get_by_label(self.data.CB_I_AGREE_LABEL).check()