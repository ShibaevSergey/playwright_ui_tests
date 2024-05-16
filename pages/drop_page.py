import allure
from playwright.sync_api import expect
from config.links import Links
from data.drop_page_data import DropPageLocators
from pages.base_page import BasePage


class DropPage(BasePage):
    locators = DropPageLocators()
    PAGE_URL = Links.DROP

