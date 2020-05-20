import time



def test_check_is_button_basket_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    btn_add_to_basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert btn_add_to_basket, "button is absent"
