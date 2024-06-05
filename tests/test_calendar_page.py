from pages.calendar_page import CalendarPage


class TestCalendarPage:
    def test_calendar_page(self, browser):
        calendar_page = CalendarPage(browser)
        calendar_page.navigate()
        calendar_page.choose_start_date_as_today()
        calendar_page.choose_date_after_three_days()
        calendar_page.expect_chosen_dates()
        calendar_page.choose_today_date_time()
        calendar_page.increase_time_two_hours()
        calendar_page.expect_datetime()
