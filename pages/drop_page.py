import allure
from playwright.sync_api import expect
from config.links import Links
from data.drop_page_data import DropPageLocators, DropPageData
from pages.base_page import BasePage


class DropPage(BasePage):
    locators = DropPageLocators()
    data = DropPageData()
    PAGE_URL = Links.DROP

    @allure.step('Проверка текста до перемещения')
    def expect_text_before_drag_and_drop(self):
        expect(self.page.locator(self.locators.DROPPABLE)).to_contain_text(self.data.TEXT_BEFORE_DROP)

    @allure.step('Перемещение одного квадрата в другой')
    def drag_and_drop_first_box_to_second_box(self):
        drag_box = self.page.locator(self.locators.DRAGGABLE)
        drop_box = self.page.locator(self.locators.DROPPABLE)
        drag_box.drag_to(drop_box)

    @allure.step('Проверка текста после перемещения')
    def expect_text_after_drag_and_drop(self):
        expect(self.page.locator(self.locators.DROPPABLE)).to_contain_text(self.data.TEXT_AFTER_DROP)
