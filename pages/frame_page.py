import allure
from config.links import Links
from data.frame_page_data import FramePageLocators, FramePageData
from pages.base_page import BasePage


class FramePage(BasePage):
    locators = FramePageLocators()
    data = FramePageData()
    PAGE_URL = Links.FRAME


    @allure.step('Ввод имени в поле "First Name" фрейма "firstFr"')
    def input_first_name_in_frame(self):
        self.page.frame_locator(self.locators.FIRST_FRAME).get_by_placeholder(
            self.data.FIRST_NAME_PLACEHOLDER).fill(self.data.FIRST_NAME)

    @allure.step('Ввод имени в поле "Last Name" фрейма "firstFr"')
    def input_last_name_in_frame(self):
        self.page.frame_locator(self.locators.FIRST_FRAME).get_by_placeholder(
            self.data.LAST_NAME_PLACEHOLDER).fill(self.data.LAST_NAME)

    @allure.step('Ввод email в поле "Email" внутреннего фрейма')
    def input_email_in_inner_frame(self):
        self.page.frame_locator(self.locators.FIRST_FRAME).frame_locator(
            self.locators.INNER_FRAME).get_by_placeholder(
            self.data.EMAIL_PLACEHOLDER).fill(self.data.EMAIL)