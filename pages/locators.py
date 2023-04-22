from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, '.product_main h1')
    MESSAGE_SUCCESS_PRICE = (By.CSS_SELECTOR,'div.alert-info')
    MESSAGE_SUCCESS_NAME = (By.CSS_SELECTOR, 'div.alert-success')
    PRODUCT_PRICE_ON_BASKET = (By.CSS_SELECTOR, 'div.alertinner strong')
    PRODUCT_NAME_ON_BASKET = (By.CSS_SELECTOR, 'div.alertinner p strong')
