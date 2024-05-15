from faker import Faker

class FramePageLocators:
    FIRST_FRAME = 'iframe[id="firstFr"]'
    INNER_FRAME = 'app-frame-content iframe'


class FramePageData:
    fake = Faker('ru_RU')
    FIRST_NAME_PLACEHOLDER = 'Enter name'
    FIRST_NAME = fake.first_name()
    LAST_NAME_PLACEHOLDER = 'Enter email'
    LAST_NAME = fake.last_name()
    EMAIL_PLACEHOLDER = 'Enter email'
    EMAIL = fake.email()