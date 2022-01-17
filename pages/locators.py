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


class InternalPageLocators:
    # Right menu elements:
    SIGN_IN = (By.CSS_SELECTOR, ".ow_signin_label")
    SIGN_UP = (By.CLASS_NAME, 'ow_console_item_link')
    USER_BOARD = (By.CLASS_NAME, 'ow_notification_list')
    USER_MENU = (By.CSS_SELECTOR, '.ow_dropdown_menu_item.ow_cursor_pointer')
    SIGN_OUT = (By.XPATH, ".//a[contains(@href, 'sign-out')]")
    USER_ICON = (By.CSS_SELECTOR, ".ow_console_items_wrap > div:nth-child(5)")
    MESSAGE = ()
    # Left menu elements:
    ACTIVE_MENU = (By.CSS_SELECTOR, ".ow_responsive_menu .ow_main_menu .active")
    MAIN_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_main_menu_index a")
    DASHBOARD_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_dashboard a")
    JOIN_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_base_join_menu_item a")
    MEMBERS_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_users_main_menu_item a")
    PHOTO_MENU = (By.CSS_SELECTOR, ".ow_site_panel .photo_photo a")
    VIDEO_MENU = (By.CSS_SELECTOR, ".ow_site_panel .video_video ")

