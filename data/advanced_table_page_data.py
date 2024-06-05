class AdvancedTablePageLocators:
    INPUT_SEARCH = 'input[type="search"]'
    ROWS_TABLE = '#advancedtable tbody tr'
    SELECT_COUNT_ROWS = 'select[name="advancedtable_length"]'
    PAGE_BUTTONS = '.paginate_button[tabindex="0"]:not([id])'
    NEXT_BTN = '.paginate_button[data-dt-idx="next"]'
    LAST_BTN = '.paginate_button[data-dt-idx="last"]'
    FIRST_BTN = '.paginate_button[data-dt-idx="first"]'
    PREVIOUS_BTN = '.paginate_button[data-dt-idx="previous"]'
    HEADERS_COLUMNS = 'th.sorting'


class AdvancedTablePageData:
    SEARCH_PATTERN = ['american', '.edu', 'london', '35']
    AMERICAN_NO = [4, 8, 35, 41]
    EDU_NO = [4, 5, 8]
    LONDON_NO = [4, 8, 9, 26, 28, 30, 32, 35, 38, 39, 40, 41, 42, 44, 45, 46]
    NO_35 = [35]
    COUNT_5 = '5'
    COUNT_10 = '10'
    COUNT_25 = '25'
    CLASS_CURRENT_PAGE = 'paginate_button current'
    CLASS = 'class'
    ASCENDING = 'ascending'
    DESCENDING = 'descending'
    SORT_ATTRIBUTE = 'aria-sort'
    S_NO = 'S.NO:'
    UNIVERSITY_NAME = 'UNIVERSITY NAME:'
    COUNTRY = 'COUNTRY:'
    WEBSITE = 'WEBSITE:'
