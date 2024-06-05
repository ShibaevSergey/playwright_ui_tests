import random
import allure
from playwright.sync_api import expect
from config.links import Links
from data.form_page_data import FormPageLocators, FormPageData
from pages.base_page import BasePage
from pytest_check import check


class FormPage(BasePage):
    locators = FormPageLocators()
    data = FormPageData()
    PAGE_URL = Links.FORM
    country_code_value = None
    country_value = None

    def expect_field_is_required(self, locator: str):
        with allure.step(f'Проверка поля {locator} на обязтельность'):
            expect(self.page.locator(locator)).to_have_attribute(self.data.REQUIRED_ATTRIBUTE, '')

    def expect_input_type(self, locator: str, input_type: str):
        with allure.step(f'Проверка типа поля: {locator}'):
            attr = self.page.locator(locator).get_attribute('type')
            with check:
                assert attr == input_type, f'Атрибут "type" ({attr}) для поля {locator} не равен {input_type}'

    def expect_input_pattern(self, locator: str, pattern: str):
        with allure.step(f'Проверка наличия паттерна {pattern} у поля {locator}'):
            expect(self.page.locator(locator)).to_have_attribute('pattern', pattern)

    @allure.step('Ввод имени')
    def fill_first_name(self):
        self.page.locator(self.locators.FIRST_NAME_INPUT).fill(self.data.FIRST_NAME)

    @allure.step('Ввод фамилии')
    def fill_last_name(self):
        self.page.locator(self.locators.LAST_NAME_INPUT).type(self.data.LAST_NAME)

    @allure.step('Ввод электронной почты')
    def fill_email(self):
        self.page.locator(self.locators.EMAIL_INPUT).fill(self.data.EMAIL)

    @allure.step('Ввод телефонного номера')
    def fill_phone_number(self):
        self.page.locator(self.locators.PHONE_NUMBER_INPUT).fill(self.data.PHONE)

    @allure.step('Ввод адреса №1')
    def fill_address_1(self):
        self.page.locator(self.locators.ADDRESS_INPUT_1).fill(self.data.ADDRESS_1)

    @allure.step('Ввод адреса №2')
    def fill_address_2(self):
        self.page.locator(self.locators.ADDRESS_INPUT_2).fill(self.data.ADDRESS_2)

    @allure.step('Ввод названия адмнистративной единицы (область)')
    def fill_state(self):
        self.page.locator(self.locators.STATE_INPUT).fill(self.data.STATE)

    @allure.step('Ввод почтового индекса')
    def fill_postal_code(self):
        self.page.locator(self.locators.POSTAL_CODE_INPUT).fill(self.data.POSTAL_CODE)

    @allure.step('Ввод даты рождения')
    def fill_birthday(self):
        self.page.locator(self.locators.DATE_OF_BIRTH).type(self.data.BIRTH_DAY)

    @allure.step('Установить пол')
    def set_sex(self):
        self.page.locator(self.data.SEX).click()

    @allure.step('Установить код страны')
    def set_country_code(self):
        options = self.page.locator(self.locators.COUNTRY_CODE_SELECT_OPTIONS).all()
        option = random.randint(0, len(options) - 1)
        self.country_code_value = options[option].get_attribute('value')
        self.page.locator(self.locators.COUNTRY_CODE_SELECT).select_option(value=self.country_code_value)

    @allure.step('Проверка выбранного кода страны')
    def expect_country_code(self):
        expect(self.page.locator(self.locators.COUNTRY_CODE_SELECT)).to_have_value(self.country_code_value)

    @allure.step('Установить страну')
    def set_country(self):
        options = self.page.locator(self.locators.COUNTRY_SELECT_OPTIONS).all()
        option = random.randint(0, len(options) - 1)
        self.country_value = options[option].get_attribute('value')
        self.page.locator(self.locators.COUNTRY_SELECT).select_option(value=self.country_value)

    @allure.step('Проверка выбранной страны')
    def expect_country(self):
        expect(self.page.locator(self.locators.COUNTRY_SELECT)).to_have_value(self.country_value)

    @allure.step('Установить чек-бокс "I agree..."')
    def check_checkbox_i_agree(self):
        self.page.locator(self.locators.I_AGREE_CHECKBOX).check()

    @allure.step('Клик на кнопку "Отправить"')
    def click_btn_submit(self):
        self.page.locator(self.locators.SUBMIT_BTN).click()