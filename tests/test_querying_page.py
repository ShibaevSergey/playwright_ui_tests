def test_button(querying_page):
    querying_page.navigate()
    querying_page.click_btn()
    querying_page.expect_btn_name()