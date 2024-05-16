import allure
from playwright.sync_api import Page, BrowserContext


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page


    def navigate(self):
        with allure.step(f'Переход на страницу {self.PAGE_URL}'):
            self.page.goto(self.PAGE_URL, wait_until='domcontentloaded')

    @allure.step('Вернуться назад')
    def go_back(self):
        self.page.go_back(wait_until='domcontentloaded')

    @allure.step('Перезагрузка страницы')
    def reload(self):
        self.page.reload(wait_until='domcontentloaded')

    def close(self):
        with allure.step(f'Закрыть вкладку {self.page.title()}'):
            self.page.close()