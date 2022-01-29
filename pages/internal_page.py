from pages.base_page import BasePage
from pages.elements.base_element import ElementObject
from pages.locators import InternalPageLocators


class InternalPage(BasePage):
    sign_in_menu = ElementObject(InternalPageLocators.SIGN_IN)
    sign_up_menu = ElementObject(InternalPageLocators.SIGN_UP)
    main_menu = ElementObject(InternalPageLocators.MAIN_MENU)
    member_menu = ElementObject(InternalPageLocators.MEMBERS_MENU)
    dashboard_menu = ElementObject(InternalPageLocators.DASHBOARD_MENU)
    user_menu = ElementObject(InternalPageLocators.USER_MENU)
    message_menu = ElementObject(InternalPageLocators.MESSAGE)

    def open_sign_in_form(self):
        self.sign_in_menu.click()

    def sign_out(self):
        """ Logout (Sign out) at Oxwall site """
        if self.is_element_present(InternalPageLocators.USER_MENU):
            self.action_chain.move_to_element(self.user_menu)
            self.action_chain.perform()
            el_sign_out = self.find_element(InternalPageLocators.SIGN_OUT)
            el_sign_out.click()
