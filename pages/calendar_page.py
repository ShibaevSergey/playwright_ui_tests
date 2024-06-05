import allure
from playwright.sync_api import expect
from config.links import Links
from data.calendar_page_data import CalendarPageLocators, CalendarPageData
from pages.base_page import BasePage
from datetime import datetime, timedelta


class CalendarPage(BasePage):
    locators = CalendarPageLocators()
    data = CalendarPageData()
    PAGE_URL = Links.CALENDAR
    today = None
    end = None

    @allure.step('Выбор сегодняшней даты как начало интервала')
    def choose_start_date_as_today(self):
        with allure.step('Открыть календарь для ввода даты (начало интервала)'):
            self.page.locator(self.locators.DATETIME_PICKER_START).click()
        with allure.step('Выбрать сегодняшний день'):
            self.page.locator(self.locators.ACTIVE_TODAY_BTN).click()
        with allure.step('Закрыть календарь'):
            self.page.locator(self.locators.ACTIVE_CLOSE_BTN).click()

    @allure.step('Выбрать дату через три дня для конца интервала')
    def choose_date_after_three_days(self):
        self.today = datetime.today()
        self.end = self.today + timedelta(days=3)
        end_data = self.end.strftime('%b %d %Y')
        self.page.locator(self.locators.DATETIME_PICKER_END).click()
        days = self.page.locator(self.locators.ACTIVE_DAYS).all()
        for day in days:
            if str(end_data) in str(day.get_attribute(self.data.DATE_ATTRIBUTE)):
                day.click()
                break

    @allure.step('Проверка выбранных дат')
    def expect_chosen_dates(self):
        text = self.page.locator(self.locators.DATE_SELECTED_TEXT)
        pattern = '%d-%b-%Y'
        today_date = self.today.strftime(pattern)
        end_date = self.end.strftime(pattern)
        expect(text).to_contain_text(today_date)
        expect(text).to_contain_text(end_date)

    @allure.step('Выбор текущих даты и времени в основном календаре с помощью кнопки "Today"')
    def choose_today_date_time(self):
        self.page.locator(self.locators.MAIN_TODAY_BTN).click()

    @allure.step('Увеличение времени на +2 часа')
    def increase_time_two_hours(self):
        self.page.locator(self.locators.TIMEPICKER_HOUR_INCREASE).click(click_count=2)

    @allure.step('Проверка установленных даты и времени')
    def expect_datetime(self):
        text = self.page.locator(self.locators.TIME_SELECTED_TEXT)
        pattern = '%#m/%#d/%y, %#I:%M %p'
        checked_datetime = datetime.today() + timedelta(hours=2)
        expect(text).to_contain_text(str(checked_datetime.strftime(pattern)))
