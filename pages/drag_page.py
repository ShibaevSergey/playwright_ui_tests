import allure
from playwright.sync_api import expect
from config.links import Links
from data.drag_page_data import DragPageLocators, DragPageData
from pages.base_page import BasePage


class DragPage(BasePage):
    locators = DragPageLocators()
    data = DragPageData()
    PAGE_URL = Links.DRAG

    @allure.step('Drag and Drop box')
    def drag_and_drop_box(self):
        box = self.page.locator(self.locators.DRAG_BOX).bounding_box()
        drag_box = self.page.locator(self.locators.DRAG_BOX)
        drag_box.hover()
        self.page.mouse.down()
        self.page.mouse.move(box['x'] + 300, box['y'] + 300)
        self.page.mouse.move(box['x'] + 300, box['y'] + 300)
        self.page.mouse.up()

    @allure.step('Проверка перемещения квадрата')
    def expect_dragged_box(self):
        drag_box = self.page.locator(self.locators.DRAG_BOX)
        expect(drag_box).to_have_attribute(self.data.ATTRIBUTE, self.data.DRAG_BOX_STYLE_AFTER_DRAG)
