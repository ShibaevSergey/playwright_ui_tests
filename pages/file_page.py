import os
import allure
from config.errors import Errors
from config.links import Links
from data.file_page_data import FilePageLocators, FilePageData
from pages.base_page import BasePage
from settings import ROOT_DIR


class FilePage(BasePage):
    locators = FilePageLocators()
    data = FilePageData()
    PAGE_URL = Links.FILE

    @allure.step('Загрузить Excel файл')
    def download_excel_file(self):
        with self.page.expect_download() as download_info:
            self.page.get_by_role(self.data.ROLE, name=self.data.DOWNLOAD_EXCEL_NAME).click()
        download = download_info.value
        download.save_as(f"{os.path.join(ROOT_DIR, self.data.DOWNLOAD_DIR)}/{download.suggested_filename}")

    @allure.step('Проверка загрузки Excel файла')
    def expect_downloading_excel_file(self):
        file_exist = os.path.isfile(os.path.join(ROOT_DIR, self.data.DOWNLOAD_DIR, self.data.EXCEL_NAME))
        assert file_exist is True, Errors.DOWNLOAD_FILE_ERROR

    @allure.step('Загрузить PDF файл')
    def download_pdf_file(self):
        with self.page.expect_download() as download_info:
            self.page.get_by_role(self.data.ROLE, name=self.data.DOWNLOAD_PDF_NAME).click()
        download = download_info.value
        download.save_as(f'{os.path.join(ROOT_DIR, self.data.DOWNLOAD_DIR)}/{download.suggested_filename}')

    @allure.step('Проверка загрузки PDF файла')
    def expect_downloading_pdf_file(self):
        file_exist = os.path.isfile(os.path.join(ROOT_DIR, self.data.DOWNLOAD_DIR, self.data.PDF_NAME))
        assert file_exist is True, Errors.DOWNLOAD_FILE_ERROR

    @allure.step('Загрузить PDF файл')
    def download_txt_file(self):
        with self.page.expect_download() as download_info:
            self.page.get_by_role(self.data.ROLE, name=self.data.DOWNLOAD_TEXT_NAME).click()
        download = download_info.value
        download.save_as(f'{os.path.join(ROOT_DIR, self.data.DOWNLOAD_DIR)}/{download.suggested_filename}')

    @allure.step('Проверка загрузки PDF файла')
    def expect_downloading_txt_file(self):
        file_exist = os.path.isfile(os.path.join(ROOT_DIR, self.data.DOWNLOAD_DIR, self.data.TEXT_NAME))
        assert file_exist is True, Errors.DOWNLOAD_FILE_ERROR

    @allure.step('Удаление скачанных файлов из папки "downloads"')
    def remove_files_from_downloads_dir(self):
        files_list = os.listdir(os.path.join(ROOT_DIR, self.data.DOWNLOAD_DIR))
        for file in files_list:
            os.remove(os.path.join(ROOT_DIR, self.data.DOWNLOAD_DIR, file))

    @allure.step('Загрузить файл')
    def upload_file(self):
        self.page.locator(self.locators.UPLOAD).set_input_files(
            os.path.join(ROOT_DIR, self.data.UPLOAD_DIR, self.data.TEST_FILE_NAME))
