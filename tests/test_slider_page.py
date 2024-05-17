from pages.slider_page import SliderPage


class TestSliderPage:
    def test_slider_page(self, browser):
        slider_page = SliderPage(browser)
        slider_page.navigate()
        slider_page.set_slider_value()
        slider_page.click_btn_get_countries()
        slider_page.expect_count_displayed_countries()