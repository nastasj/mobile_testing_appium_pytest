from .base_page import BasePage
from .locators import CatalogPageLocators


class CatalogPage(BasePage):

    def choose_product_from_catalog(self):
        self.click_on_element(*CatalogPageLocators.TO_CATALOG_BUTTON)
        self.driver.find_elements(*CatalogPageLocators.CATALOG_ELEMENT)[0].click()
        self.is_appeared(*CatalogPageLocators.CATALOG_ELEMENT)
        self.driver.find_elements(*CatalogPageLocators.CATALOG_ELEMENT)[2].click()
        self.is_appeared(*CatalogPageLocators.CATALOG_ELEMENT)
        self.driver.find_elements(*CatalogPageLocators.CATALOG_ELEMENT)[3].click()
        self.click_on_element(*CatalogPageLocators.CHOOSE_PRODUCT_BUTTON)