from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from custom_expected_condidion import presence_of_elements_located_by_number
from pages.locators import *


class OxwallApp:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3, poll_frequency=0.1)
        self.action_chain = webdriver.ActionChains(self.driver)

    def sign_in(self, user):
        login_elem = self.driver.find_element(USERNAME_FIELD)
        login_elem.clear()
        login_elem.send_keys(user["username"])

        pass_elem = self.driver.find_element(PASSWORD_FIELD)
        pass_elem.clear()
        pass_elem.send_keys(user["password"])

        sign_in_button = self.driver.find_element(SING_IN_BTN)
        sign_in_button.click()

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
