from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Page has not login url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER)
        user_email.send_keys(email)
        user_password = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER)
        user_password.send_keys(password)
        password_required = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_2)
        password_required.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT).click()

