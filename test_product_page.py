from pages.product_page import ProductPage
from pages.main_page import MainPage
import pytest
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Wrong name')) for i in range(10)])
def test_user_can_add_product_to_basket(browser, promo_offer):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}'
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.name_of_the_book_in_basket_and_main_page_should_be_same()
    page.price_of_the_book_in_basket_and_main_page_should_be_same()
    page.success_messages_should_be_presented()