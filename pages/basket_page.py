from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def product_basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Message is not presented'

    def should_be_a_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), 'Success message is not disappeared, but should be'



