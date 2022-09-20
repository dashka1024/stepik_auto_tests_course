from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_add_button(browser):
    browser.get(link)
    time.sleep(30)
    x=browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert x is not None, "Кнопки нет"