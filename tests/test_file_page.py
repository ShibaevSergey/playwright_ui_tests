from pages.file_page import FilePage


class TestFilePage:
    def test_file_page_downloads(self, browser):
        file_page = FilePage(browser)
        file_page.navigate()
        file_page.download_excel_file()
        file_page.download_pdf_file()
        file_page.download_txt_file()
        file_page.expect_downloading_excel_file()
        file_page.expect_downloading_pdf_file()
        file_page.expect_downloading_txt_file()
        file_page.remove_files_from_downloads_dir()

    def test_file_page_upload(self, browser):
        file_page = FilePage(browser)
        file_page.navigate()
        file_page.upload_file()
