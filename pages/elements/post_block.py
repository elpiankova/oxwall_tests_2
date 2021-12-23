from selenium.webdriver.remote.webelement import WebElement

from pages.locators import PostBlockLocators
from value_objects.user import User


class PostBlock:
    def __init__(self, element: WebElement):
        self.element = element

    @property
    def text(self):
        return self.element.find_element(*PostBlockLocators.POST_TEXT).text

    @property
    def user(self):
        el = self.element.find_element(*PostBlockLocators.POST_USER)
        real_name = el.text
        username = el.get_attribute("href").split("/")[-1]
        return User(username=username, real_name=real_name)

    @property
    def time_created(self):
        return self.element.find_element(*PostBlockLocators.POST_TIME).text

    @property
    def likes_bt(self):
        # TODO find like element
        pass

    def likes_count(self):
        pass

    def add_like(self):
        self.likes_bt.click()

    def add_comment(self, text):
        pass

