from selenium import webdriver
import time

def open_browser(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    return browser

def close_browser():
    time.sleep(5)
    browser.quit()

link = "http://suninjuly.github.io/cats.html"

try:
    browser = open_browser(link)
    button = browser.find_element_by_id("button")

finally:
    close_browser()