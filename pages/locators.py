from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK_NAME_ON_BASKET = (By.CSS_SELECTOR, '.alert-success:first-child')
    PRICE_ON_BASKET = (By.CSS_SELECTOR, '.alert-info strong')
    BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    BOOK_NAME_ON_PAGE = (By.CSS_SELECTOR, '.product_main > h1')
    SUCCESS_MESSAGES = (By.ID, 'messages')

    
    