import os
from dotenv import load_dotenv

load_dotenv()

class QueryingPageLocators:
    BUTTON_BTN = '#query-btn'
    DIV_WITH_DATA_TEST_ID = 'div[data-test-id="test-example"]'
    INPUT_NAME = '#inputName'
    QUERY_FORM = '.query-form'
    INPUT_EMAIL = '#inputEmail'
    SUBMIT_BTN = 'button[data-cy="submit"]'

class QueryingPageData:
    BTN_NAME = 'Button'
    CLASS_DIV_WITH_DATA_TEST_ID = 'example'
    APPLES = 'apples'
    ORANGES = 'oranges'
    BANANAS = 'bananas'
    MORE_APPLES = 'more apples'
    APPLES_CLASS = 'first'
    ORANGES_CLASS = 'second'
    BANANAS_CLASS = 'third'
    MORE_APPLES_CLASS = 'fourth'
    BTN_SAVE_FROM_NAME = 'Save Form'
    BTN_SAVE_FROM_NAME_CLASS = 'btn btn-default'
    FILL_NAME = 'Иван'
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    PASSWORD_PLACEHOLDER = 'Password'
