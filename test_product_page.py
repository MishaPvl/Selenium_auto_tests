from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


# @pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Wrong name')) for i in range(10)])
# def test_user_can_add_product_to_basket(browser, promo_offer):
#     link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}'
#     page = ProductPage(browser, link)
#     page.open()
#     page.guest_can_add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.name_of_the_book_in_basket_and_main_page_should_be_same()
#     page.price_of_the_book_in_basket_and_main_page_should_be_same()
#     page.success_messages_should_be_presented()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message_before_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.message_should_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.product_basket_should_be_empty()
    basket_page.should_be_a_message_about_empty_basket()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.register_new_user('abcc@gmail.com', 'ws12d5110f')
        self.login_page.should_be_authorized_user()
        
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.guest_can_add_product_to_basket()
        page.name_of_the_book_in_basket_and_main_page_should_be_same()
        page.price_of_the_book_in_basket_and_main_page_should_be_same()
        page.success_messages_should_be_presented()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.guest_can_add_product_to_basket()
        page.should_not_be_success_message()