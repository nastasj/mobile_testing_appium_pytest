from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def open_browser(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    return browser

def close_browser():
    time.sleep(5)
    browser.quit()

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = open_browser(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    close_browser()