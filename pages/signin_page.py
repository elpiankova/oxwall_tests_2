from pages.locators import *
from pages.base_page import BasePage


class SignInPage(BasePage):
    def input_username(self, username):
        login_elem = self.driver.find_element(*USERNAME_FIELD)
        login_elem.clear()
        login_elem.send_keys(username)

    def input_password(self, password):
        pass_elem = self.driver.find_element(*PASSWORD_FIELD)
        pass_elem.clear()
        pass_elem.send_keys(password)

    def press_sign_in(self):
        sign_in_button = self.driver.find_element(*SING_IN_BTN)
        sign_in_button.click()

    def submit(self):
        # TODO press Enter
        pass

    def sign_in(self, user):
        self.input_username(user['username'])
        self.input_password(user['password'])
        self.press_sign_in()
