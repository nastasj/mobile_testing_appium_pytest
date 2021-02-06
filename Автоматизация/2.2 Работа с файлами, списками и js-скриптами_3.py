from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = " http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # x = browser.find_element_by_id("num1").text
    # y = browser.find_element_by_id("num2").text
    s = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(s))
    button = browser.find_element_by_css_selector(".btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()