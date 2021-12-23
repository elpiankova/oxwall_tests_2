from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from custom_expected_condidion import presence_of_elements_located_by_number
from pages.elements.base_element import ElementsObject, ElementObject, PostElementsObjects
from pages.elements.post_block import PostBlock
from pages.locators import DashboardLocators
from pages.base_page import BasePage


class DashboardPage(BasePage):
    new_post_text_field = ElementObject(DashboardLocators.POST_INPUT)
    send_button = ElementObject(DashboardLocators.SEND_BTN)
    posts = PostElementsObjects(DashboardLocators.POST_BLOCK)

    # @property
    # def new_post_text_field(self):
    #     return self.find_element(DashboardLocators.POST_INPUT)
    #
    # @property
    # def send_button(self):
    #     return self.find_element(DashboardLocators.SEND_BTN)
    #
    # @property
    # def posts(self):
    #     elms = self.find_elements(DashboardLocators.POST_BLOCK)
    #     post_blocks = [PostBlock(el) for el in elms]
    #     return post_blocks

    def count_posts(self):
        return len(self.posts)

    def create_new_text_post(self, input_text):
        self.new_post_text_field.click()
        self.new_post_text_field.send_keys(input_text)
        self.send_button.click()

    def wait_new_post(self, old_number_of_post: int):
        """
        Wait new post appears
        :param old_number_of_post: amount posts before create new one
        :return:
        """
        new_number = old_number_of_post + 1
        new_list_of_posts = self.wait.until(
            presence_of_elements_located_by_number(DashboardLocators.POST_BLOCK, new_number),
            message=f"Not find {new_number} post elements")
        post_blocks = [PostBlock(el) for el in new_list_of_posts]
        return post_blocks

    def title(self):
        return self.driver.title
