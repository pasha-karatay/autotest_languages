def test_guest_should_see_login_link_pass(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element_by_css_selector("#add_to_basket_form > button")
