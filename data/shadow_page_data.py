from faker import Faker


class ShadowPageLocators:
    FIRST_NAME = '#fname'
    LAST_NAME = 'my-web-component'
    EMAIL = 'div[class="field"]:nth-child(3)'


class ShadowPageData:
    fake = Faker('ru_RU')
    FIRST_NAME = fake.first_name()
    LAST_NAME = fake.last_name()
    EMAIL = fake.email()
