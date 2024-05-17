import allure
from playwright.sync_api import Page, Locator


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

    def pause(self, timeout: int):
        with allure.step(f'Пауза на {timeout} миллисекунд'):
            self.page.wait_for_timeout(timeout)

    @allure.step('Перенос одного элемента к другому')
    def drag_and_drop(self, source: Locator, target: Locator):
        source.hover()
        self.page.mouse.down()
        target.hover()
        target.hover()
        self.page.mouse.up()


