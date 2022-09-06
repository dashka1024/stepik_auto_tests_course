from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	button = browser.find_element(By.CSS_SELECTOR, '.btn')
	button.click()
	confirm = browser.switch_to.alert
	confirm.accept()
	x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
	y = calc(x)
	input_y = browser.find_element(By.CSS_SELECTOR, "#answer")
	input_y.send_keys(str(y))
	button = browser.find_element(By.CSS_SELECTOR, '.btn')
	button.click()


finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(30)
	# закрываем браузер после всех манипуляций
	browser.quit()