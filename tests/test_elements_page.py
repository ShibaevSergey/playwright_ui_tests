from pages.elements_page import ElementsPage


class TestElementsPage:
    def test_elements_page(self, browser):
        elements_page = ElementsPage(browser)
        elements_page.navigate()
        elements_page.fill_github_nickname()
        elements_page.click_btn_search()
        elements_page.expect_img_profile()
        elements_page.print_all_info_about_profile()
        elements_page.expect_repo_links_count()