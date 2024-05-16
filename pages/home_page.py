import allure
from pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step('Напечатать заголовок страницы')
    def print_title_page(self):
        self.page.wait_for_timeout(1000)
        title = self.page.title()
        print(title)
        allure.attach(title, 'Заголовок страницы', allure.attachment_type.TEXT)
