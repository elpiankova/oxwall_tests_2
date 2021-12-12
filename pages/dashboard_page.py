from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from custom_expected_condidion import presence_of_elements_located_by_number
from pages.locators import *
from pages.base_page import BasePage


class DashboardPage(BasePage):
    #TODO locators extract
    def count_posts(self):
        # Count posts
        posts = self.driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
        return len(posts)

    def create_new_text_post(self, input_text):
        new_post_elem = self.wait.until(ec.presence_of_element_located((By.NAME, "status")),
                                   message="Can't find new post text area")
        new_post_elem.click()
        new_post_elem.send_keys(input_text)

        send_button = self.driver.find_element(By.NAME, "save")
        send_button.click()

    def wait_new_post(self, old_number_of_post: int):
        """
        Wait new post appears
        :param old_number_of_post: amount posts before create new one
        :return:
        """
        wait = WebDriverWait(self.driver, 3, poll_frequency=0.1)
        new_number = old_number_of_post + 1
        new_list_of_posts = wait.until(
            presence_of_elements_located_by_number((By.CLASS_NAME, "ow_newsfeed_item"), new_number),
            message=f"Not find {new_number} post elements")
        return new_list_of_posts

    def title(self):
        return self.driver.title
