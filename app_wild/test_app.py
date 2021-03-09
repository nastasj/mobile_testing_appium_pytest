from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.catalog_page import CatalogPage
from .pages.product_page import ProductPage
import pytest
import time

class TestApp:

    def test_choose_product_from_catalog_and_add_to_basket(self, driver):
        page = BasePage(driver)
        page.after_installation()
        catalog_page = CatalogPage(driver)
        catalog_page.choose_product_from_catalog()
        product_page = ProductPage(driver)
        product_page.add_to_basket()
        basket_page = BasketPage(driver)
        basket_page.in_basket()
