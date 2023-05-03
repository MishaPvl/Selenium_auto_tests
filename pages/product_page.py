from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        self.name_on_main_page = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_PAGE).text
        self.price_on_main_page = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_PAGE).text
        add_button.click()

    def name_of_the_book_in_basket_and_main_page_should_be_same(self):
        name_on_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_BASKET).text
        assert self.name_on_main_page == name_on_basket, 'Name of the book in the basket and on the page are different'
    
    def price_of_the_book_in_basket_and_main_page_should_be_same(self):
        price_on_basket = self.browser.find_element(*ProductPageLocators.PRICE_ON_BASKET).text
        assert price_on_basket == self.price_on_main_page, 'Price of the book in the basket and on the page are different'

    def success_messages_should_be_presented(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), 'Success messages is not presented'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is not disappeared, but should be'