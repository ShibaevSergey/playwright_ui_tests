import allure
import pytest
from playwright.sync_api import expect

from config.errors import Errors
from config.links import Links
from data.button_page_data import ButtonPageLocators, ButtonPageData
from pages.base_page import BasePage


class ButtonPage(BasePage):
    locators = ButtonPageLocators()
    data = ButtonPageData()
    PAGE_URL = Links.BUTTON

    @allure.step('Клик на кнопку "Home"')
    def click_btn_home(self):
        self.page.locator(self.locators.HOME_BTN).click()

    @allure.step('Проверить координаты x и y кнопки')
    def expect_x_and_y_coords_btn(self):
        box = self.page.locator(self.locators.POSITION_BTN).bounding_box()
        assert box['x'] == self.data.POSITION_BTN_X, Errors.COORD_X_ERROR
        assert box['y'] == self.data.POSITION_BTN_Y, Errors.COORD_Y_ERROR

    @allure.step('Проверка цвета кнопки')
    def expect_color_btn(self):
        self.page.locator(self.locators.COLOR_BTN)

    @allure.step('Проверить ширину и длину кнопки')
    def expect_width_and_height_btn(self):
        box = self.page.locator(self.locators.PROPERTY_BTN).bounding_box()
        assert round(box['width']) == round(self.data.POSITION_BTN_WIDTH), Errors.WIDTH_ERROR
        assert box['height'] == self.data.POSITION_BTN_HEIGHT, Errors.HEIGHT_ERROR

    @allure.step('Проверка цвета кнопки')
    def expect_color_btn(self):
        expect(self.page.locator(self.locators.COLOR_BTN)).to_have_css('background-color', self.data.COLOR_BTN_RGB)

    @allure.step('Проверка активности кнопки')
    def expect_btn_disable(self):
        expect(self.page.locator(self.locators.DISABLED_BTN).filter(
            has_text=self.data.DISABLED_BTN_NAME)).to_have_attribute('disabled', '')

    @allure.step('Клик и удержание на кнопку')
    def click_and_hold_button(self):
        self.page.locator(self.locators.DISABLED_BTN).filter(
            has_not_text=self.data.DISABLED_BTN_NAME).click(delay=1000)

    @allure.step('Проверка текста в кнопке')
    def expect_text_in_hold_button(self):
        expect(self.page.locator(self.locators.DISABLED_BTN).filter(
            has_not_text=self.data.DISABLED_BTN_NAME)).to_contain_text(self.data.AFTER_HOLD_BTN_NAME)