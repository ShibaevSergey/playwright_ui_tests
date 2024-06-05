from pages.shadow_page import ShadowPage


class TestShadowPage:
    def test_shadow_page(self, browser):
        shadow_page = ShadowPage(browser)
        shadow_page.navigate()
        shadow_page.input_first_name()
        shadow_page.input_last_name()
        shadow_page.input_email()