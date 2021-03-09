from .base_page import BasePage
from .locators import BasketPageLocators
from .product_page import ProductPage


class BasketPage(BasePage):

    def in_basket(self):
        self.click_on_element(*BasketPageLocators.TO_BASKET_BUTTON)

