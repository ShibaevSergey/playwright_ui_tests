import allure
from config.links import Links
from data.sort_page_data import SortPageLocators, SortPageData
from pages.base_page import BasePage


class SortPage(BasePage):
    locators = SortPageLocators()
    data = SortPageData()
    PAGE_URL = Links.SORT

    def move_element_to_done(self, element_name: str):
        with allure.step(f'Пермещение элемента {element_name} в блок {self.data.DONE}'):
            drag_element = self.page.get_by_text(element_name)
            done_elements = self.page.locator(self.locators.DONE_ELEMENTS)
            list_done_elements = done_elements.all()
            if len(list_done_elements) != 0:
                drop_target = done_elements.first
            else:
                drop_target = self.page.locator(self.locators.EMPTY_DONE_ELEMENTS_GROUP)
            self.drag_and_drop(drag_element, drop_target)
            self.pause(500)

    def move_element_to_do(self, element_name: str):
        with allure.step(f'Перемещение элемента {element_name} в блок {self.data.TO_DO}'):
            drag_element = self.page.get_by_text(element_name)
            to_do_elements = self.page.locator(self.locators.TO_DO_ELEMENTS)
            list_to_do_elements = to_do_elements.all()
            if len(list_to_do_elements) != 0:
                drop_target = to_do_elements.first
            else:
                drop_target = self.page.locator(self.locators.EMPTY_TO_DO_ELEMENTS_GROUP)
            self.drag_and_drop(drag_element, drop_target)
            self.pause(500)

    def move_drag_under_drop(self, drag_element: str, drop_element: str):
        with allure.step(f'Перенос элемента {drag_element} под элемент {drop_element}'):
            drag = self.page.get_by_text(drag_element)
            drop = self.page.get_by_text(drop_element)
            box = drop.bounding_box()
            drag.hover()
            self.page.mouse.down()
            self.page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'])
            self.page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'])
            self.page.mouse.up()
            self.pause(500)

    def move_drag_above_drop(self, drag_element: str, drop_element: str):
        with allure.step(f'Перенос элемента {drag_element} над элементом {drop_element}'):
            drag = self.page.get_by_text(drag_element)
            drop = self.page.get_by_text(drop_element)
            box = drop.bounding_box()
            drag.hover()
            self.page.mouse.down()
            self.page.mouse.move(box['x'], box['y'])
            self.page.mouse.move(box['x'], box['y'])
            self.page.mouse.up()
            self.pause(500)