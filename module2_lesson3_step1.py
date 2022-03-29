from selenium import webdriver
from math import log, fabs, sin

link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button_for_alert = browser.find_element_by_css_selector("button.btn")
button_for_alert.click()

al = browser.switch_to.alert
al.accept()

value = browser.find_element_by_id('input_value')
send_answer = browser.find_element_by_id('answer')
send_answer.send_keys(log(fabs(12*sin(int(value.text)))))

button = browser.find_element_by_css_selector("button.btn")
button.click()