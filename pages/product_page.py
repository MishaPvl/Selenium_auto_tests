from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()
    
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ON_PAGE), 'Product name is not presented'
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE), 'Product price is not presented'
        assert self.is_element_present(*ProductPageLocators.MESSAGE_SUCCESS_NAME), 'Message with product name is not presented'
        assert self.is_element_present(*ProductPageLocators.MESSAGE_SUCCESS_PRICE), 'Message with price is not presented'

    def price_on_basket_and_page_should_be_same(self):
        pass
