from selenium.webdriver.common.by import By


class BasePageLocators:

    CHOOSE_COUNTRY = (By.ID, 'com.wildberries.ru:id/country_text')
    SKIP_BUTTON = (By.ID, 'com.wildberries.ru:id/skip')


class CatalogPageLocators:

    TO_CATALOG_BUTTON = (By.ID, 'com.wildberries.ru:id/btnCatalogue')
    SEARCH_FIELD = (By.ID, 'com.wildberries.ru:id/searchPlaceholder')
    CATALOG_ELEMENT = (By.ID, 'com.wildberries.ru:id/name')
    CHOOSE_PRODUCT_BUTTON = (By.ID, 'com.wildberries.ru:id/nameTitle')


class ProductPageLocators:

    ADD_TO_BASKET_BUTTON = (By.ID, 'com.wildberries.ru:id/addToBasket')
    ADD_TO_BASKET_BUTTON_2 = (By.ID, 'com.wildberries.ru:id/buttonMoveTo')
    CHOOSE_SIZE_BUTTON = (By.ID, 'com.wildberries.ru:id/sizeName')
    ARTICLE_VALUE = (By.ID, 'com.wildberries.ru:id/articleValue')

class BasketPageLocators:

    TO_BASKET_BUTTON = (By.ID, 'com.wildberries.ru:id/btnBasket')
    BASKET_ARTICLE_VALUE = (By.ID, 'com.wildberries.ru:id/productArticleValue')