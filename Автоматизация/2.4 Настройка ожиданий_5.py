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

link = "http://suninjuly.github.io/wait1.html"

try:
    browser = open_browser(link)
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
    assert "successful" in message.text

finally:
    close_browser()