from selenium import webdriver
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'tst.txt') 


link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element_by_css_selector("[name='firstname']")
first_name.send_keys('Василий')

last_name = browser.find_element_by_css_selector("[name='lastname']")
last_name.send_keys('Пупкин')

email = browser.find_element_by_css_selector("[name='email']")
email.send_keys('pup@ya.ru')

simple_file = browser.find_element_by_css_selector("[type='file']")
simple_file.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()