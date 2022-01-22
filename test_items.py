from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_guest_should_see_button_add_basket(browser):
    browser.get(link)
    time.sleep(30)
    button=browser.find_elements_by_css_selector("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert  len(button) != 1, "Button not found"
    