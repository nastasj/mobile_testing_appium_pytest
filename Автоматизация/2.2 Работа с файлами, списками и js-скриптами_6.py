from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()