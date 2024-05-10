from faker import Faker


class InputPageLocators:
    FULL_NAME = '#fullName'
    APPEND_TEXT = '#join'
    TEXT_BOX_FOR_GET_TEXT = '#getMe'
    CLEAR_TBX = '#clearMe'
    DISABLE_TBX = '#noEdit'
    DONT_WRITE = '#dontwrite'

class InputPageData:
    fake = Faker('ru_RU')
    FIRST_NAME = fake.first_name()
    LAST_NAME = fake.last_name()
    GETTING_TEXT = 'ortonikc'
    READONLY = 'readonly'
    TEXT_READONLY = 'This text is readonly'