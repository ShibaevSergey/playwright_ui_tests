


def test_button(querying_page):
    querying_page.navigate()
    querying_page.click_btn()
    querying_page.expect_btn_name()

def test_div(querying_page):
    querying_page.navigate()
    querying_page.get_class_from_data_test_id()

def test_get_element_from_text(querying_page):
    querying_page.navigate()
    querying_page.expect_class_elements_from_text()
    querying_page.expect_class_element_from_role()

def test_fill_query_form(querying_page):
    querying_page.navigate()
    querying_page.input_name()
    querying_page.input_email()
    querying_page.input_password()

def test_click_btn_submit(querying_page):
    querying_page.navigate()
    querying_page.click_btn_submit()