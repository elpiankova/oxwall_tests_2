from pages.elements.base_element import ElementObject
from pages.locators import SignInLocators, InternalPageLocators
from pages.base_page import BasePage
from value_objects.user import User


class SignInPage(BasePage):
    login_elem = ElementObject(SignInLocators.USERNAME_FIELD)
    pass_elem = ElementObject(SignInLocators.PASSWORD_FIELD)
    sign_in_button = ElementObject(SignInLocators.SING_IN_BTN)

    def input_username(self, username):
        # self.login_elem.input(username)
        self.login_elem.clear()
        self.login_elem.send_keys(username)

    def input_password(self, password):
        self.pass_elem.clear()
        self.pass_elem.send_keys(password)

    def press_sign_in(self):
        self.sign_in_button.click()

    def submit(self):
        # TODO press Enter
        pass

    def sign_in(self, user: User):
        self.input_username(user.username)
        self.input_password(user.password)
        self.press_sign_in()

    def wait_next_page(self):
        self.find_visible_element(InternalPageLocators.ACTIVE_MENU)
