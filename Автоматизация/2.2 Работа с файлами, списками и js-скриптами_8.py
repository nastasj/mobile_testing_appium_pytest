from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("ip@mail.ru")
    with open('test1.txt', 'w') as file:
        file.write('')
    path = os.getcwd() + '/' + file.name
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(path)
    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()