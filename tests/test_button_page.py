import time

from pages.button_page import ButtonPage


class TestButtonPage:
    def test_button_page(self, browser):
        button_page = ButtonPage(browser)
        button_page.navigate()
        button_page.click_btn_home()
        button_page.go_back()
        button_page.print_x_and_y_coords_btn()
        button_page.expect_color_btn()
        button_page.expect_width_and_height_btn()
        button_page.expect_btn_disable()
        button_page.click_and_hold_button()
        button_page.expect_text_in_hold_button()