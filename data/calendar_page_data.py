class CalendarPageLocators:
    DATETIME_PICKER_START = '.is-datetimepicker-range'
    DATETIME_PICKER_END = '//*[@class="datetimepicker-dummy is-primary"]/div/input[2]'
    MAIN_CALENDAR = 'div[class="column is-7-desktop is-8-tablet"] div[class="column"]:nth-child(1) .datetimepicker'
    ACTIVE_CALENDAR = 'div[class="column is-7-desktop is-8-tablet"] div[class="column"]:nth-child(2) .datetimepicker'
    ACTIVE_TODAY_BTN = f'{ACTIVE_CALENDAR} .datetimepicker-footer-today'
    MAIN_TODAY_BTN = f'{MAIN_CALENDAR} .datetimepicker-footer-today'
    ACTIVE_CLOSE_BTN = f'{ACTIVE_CALENDAR} .datetimepicker-footer-cancel'
    ACTIVE_DAYS = f'{ACTIVE_CALENDAR} .datepicker-days .datepicker-date'
    TIME_SELECTED_TEXT = 'div[class="column is-7-desktop is-8-tablet"] div[class="content has-text-centered"]:nth-child(2)'
    DATE_SELECTED_TEXT = 'div[class="column is-7-desktop is-8-tablet"] div[class="content has-text-centered"]:nth-child(3)'
    TIMEPICKER_HOUR_INCREASE = '.timepicker-hours .timepicker-next'


class CalendarPageData:
    DATE_ATTRIBUTE = 'data-date'
