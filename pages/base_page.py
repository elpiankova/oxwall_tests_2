from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3, poll_frequency=0.1)
        self.action_chain = webdriver.ActionChains(self.driver)
