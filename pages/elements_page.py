import allure
import os
from playwright.sync_api import expect

from config.errors import Errors
from config.links import Links
from data.elements_page_data import ElementsPageLocators, ElementsPageData
from pages.base_page import BasePage
from dotenv import load_dotenv


class ElementsPage(BasePage):
    locators = ElementsPageLocators()
    data = ElementsPageData()
    PAGE_URL = Links.ELEMENTS
    links_repos = None
    load_dotenv()

    @allure.step('Ввод GitHub nickname')
    def fill_github_nickname(self):
        self.page.get_by_placeholder(self.data.INPUT_PLACEHOLDER).fill(os.getenv('GH_NICK'))

    @allure.step('Клик на кнопку "Search"')
    def click_btn_search(self):
        self.page.locator(self.locators.BTN_SEARCH).click()

    @allure.step('Проверка отображения изображения профилья GitHub')
    def expect_img_profile(self):
        self.page.wait_for_selector(self.locators.IMG)
        expect(self.page.locator(self.locators.IMG)).to_be_visible()

    @allure.step('Вывести всю доступную информацию о профиле')
    def print_all_info_about_profile(self):
        profile_name = self.page.get_by_placeholder(self.data.INPUT_PLACEHOLDER).input_value()
        tags_names = self.page.locator(self.locators.TAGS_NAMES).all()
        tags_values = self.page.locator(self.locators.TAGS_VALUES).all()
        for i in range(len(tags_names)):
            print(tags_names[i].inner_text(), tags_values[i].inner_text())
        self.page.wait_for_selector(self.locators.GIT_REPOS)
        self.links_repos = self.page.locator(self.locators.GIT_REPOS).all()
        for i in self.links_repos:
            print(i.inner_text())

    @allure.step('Проверка ссылок на репозитории')
    def expect_repo_links_count(self):
        assert len(self.links_repos) == os.getenv('GH_COUNT_PUBLICK_REPO'), Errors.GH_COUNT_REPO
