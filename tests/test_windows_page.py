from pages.windows_page import WindowsPage
from pages.home_page import HomePage


class TestWindowsPage:
    def test_windows_page_home_page(self, context):
        page = context.new_page()
        windows_page = WindowsPage(page)
        windows_page.navigate()
        new_page = windows_page.wait_new_tab(context)
        home_page = HomePage(new_page)
        home_page.print_title_page()
        windows_page.close()
        home_page.close()

    def test_windows_page_multiple_windows(self, context):
        page = context.new_page()
        windows_page = WindowsPage(page)
        windows_page.navigate()
        windows_page.click_btn_multiple_windows()
        windows_page.expect_url_open_tabs(context)
        windows_page.close_all_tabs(context)
