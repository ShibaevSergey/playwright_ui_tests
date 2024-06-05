import random
import re
from faker import Faker


class FormPageLocators:
    FIRST_NAME_INPUT = '#firstname'
    LAST_NAME_INPUT = '#lasttname'
    EMAIL_INPUT = '#email'
    COUNTRY_CODE_SELECT = 'div[class="columns container"]:nth-child(2) select'
    COUNTRY_CODE_SELECT_OPTIONS = f'{COUNTRY_CODE_SELECT} option'
    PHONE_NUMBER_INPUT = '#Phno'
    ADDRESS_INPUT_1 = '#Addl1'
    ADDRESS_INPUT_2 = '#Addl2'
    STATE_INPUT = '#state'
    POSTAL_CODE_INPUT = '#postalcode'
    COUNTRY_SELECT = 'div[class="columns container"]:nth-child(5) select'
    COUNTRY_SELECT_OPTIONS = f'{COUNTRY_SELECT} option'
    DATE_OF_BIRTH = '#Date'
    MALE_RB = '#male'
    FEMALE_RB = '#female'
    TRANS_RB = '#trans'
    I_AGREE_CHECKBOX = '.checkbox input[type="checkbox"]'
    SUBMIT_BTN = 'input[type="submit"]'


class FormPageData:
    faker = Faker('ru_RU')

    @staticmethod
    def get_random_sex():
        random_sex = [FormPageLocators.MALE_RB, FormPageLocators.FEMALE_RB, FormPageLocators.TRANS_RB]
        return random_sex[random.randint(0, len(random_sex) - 1)]

    SEX = get_random_sex()
    FIRST_NAME = faker.first_name()
    LAST_NAME = faker.last_name()
    EMAIL = faker.email()
    PHONE = re.sub(r'\D', '', faker.phone_number())[1:]
    ADDRESS_1 = faker.address()
    ADDRESS_2 = faker.address()
    POSTAL_CODE = faker.postcode()
    STATE = faker.administrative_unit()
    BIRTH_DAY = faker.date_of_birth().strftime('%d%m%Y')
    REQUIRED_ATTRIBUTE = 'required'
    TYPE_EMAIL = 'email'
    TYPE_TEXT = 'text'
    TYPE_PHONE = 'tel'
    TYPE_DATE = 'date'
    EMAIL_PATTERN = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    PHONE_PATTERN = r'[123456789][0-9]{9}'

