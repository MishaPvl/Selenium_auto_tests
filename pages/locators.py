from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK_NAME_ON_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRICE_ON_BASKET = (By.CSS_SELECTOR, '.alert-info strong')
    BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    BOOK_NAME_ON_PAGE = (By.CSS_SELECTOR, '.product_main > h1')
    SUCCESS_MESSAGES = (By.ID, 'messages')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group > a')

class BasketPageLocators():
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    