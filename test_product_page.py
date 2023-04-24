from pages.product_page import ProductPage
from pages.main_page import MainPage
import time
from selenium.webdriver.common.by import By

def test_user_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.name_of_the_book_in_basket_and_main_page_should_be_same()
    page.price_of_the_book_in_basket_and_main_page_should_be_same()
    page.success_messages_should_be_presented()