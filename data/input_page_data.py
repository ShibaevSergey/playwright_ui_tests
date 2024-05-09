from faker import Faker


class InputPageLocators:
    FULL_NAME = '#fullName'
    APPEND_TEXT = '#join'

class InputPageData:
    fake = Faker('ru_RU')
    FIRST_NAME = fake.first_name()
    LAST_NAME = fake.last_name()
