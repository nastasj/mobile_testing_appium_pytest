from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def open_browser(link):
    browser = webdriver.Chrome()
    browser.get(link)
    return browser

def close_browser():
    time.sleep(5)
    browser.quit()

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = open_browser(link)
    browser.find_element_by_class_name("trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    close_browser()