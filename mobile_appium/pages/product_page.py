from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        # art1 = self.driver.find_element(*ProductPageLocators.ARTICLE_VALUE).text
        self.click_on_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.click_on_element(*ProductPageLocators.CHOOSE_SIZE_BUTTON)
        self.click_on_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON_2)
