import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self):
        with allure.step(f'Переход на страницу {self.PAGE_URL}'):
            self.page.goto(self.PAGE_URL)