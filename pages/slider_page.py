import random
import allure
from config.errors import Errors
from config.links import Links
from data.slider_page_data import SliderPageLocators
from pages.base_page import BasePage


class SliderPage(BasePage):
    locators = SliderPageLocators()
    random_steps = random.randint(1, 50)
    PAGE_URL = Links.SLIDER

    def set_slider_value(self):
        with allure.step(f'Установить значение {self.random_steps} в слайдер'):
            slider = self.page.locator(self.locators.SLIDER)
            box = slider.bounding_box()
            step = (box['width'] * 0.98) / 50
            self.page.mouse.click(box['x'] + self.random_steps * step, box['y'] + box['height'] / 2)

    @allure.step('Клик на кнопку "Get Countries"')
    def click_btn_get_countries(self):
        self.page.locator(self.locators.GET_COUNTRIES_BTN).click()

    @allure.step('Проверка количества отображенных стран')
    def expect_count_displayed_countries(self):
        self.page.wait_for_selector(self.locators.COUNTRIES_LIST)
        countries = self.page.locator(self.locators.COUNTRIES_LIST).text_content()
        assert self.random_steps == len(countries.split(' - ')), Errors.COUNTRIES_COUNT_ERROR
