
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage:

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def is_appeared(self, how, what, timeout=2):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def click_on_element(self, how, what):
        self.driver.find_element(how, what).click()

    def click_on_element_from_list(self, how, what):
        list = self.driver.find_elements(how, what)

    def after_installation(self):
        self.click_on_element(*BasePageLocators.CHOOSE_COUNTRY)
        self.click_on_element(*BasePageLocators.SKIP_BUTTON)
