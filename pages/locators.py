from selenium.webdriver.common.by import By


class SignInLocators:
    USERNAME_FIELD = (By.NAME, "identity")
    PASSWORD_FIELD = (By.NAME, "password")
    SING_IN_BTN = (By.NAME, "submit")


class DashboardLocators:
    POST_INPUT = (By.NAME, "status")
    SEND_BTN = (By.NAME, "save")
    POST_BLOCK = (By.CLASS_NAME, "ow_newsfeed_item")


class PostBlockLocators:
    POST_TEXT = (By.CLASS_NAME, "ow_newsfeed_content")
    POST_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    POST_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
