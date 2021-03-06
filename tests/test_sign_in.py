import allure

from value_objects.user import User


@allure.title("Sign in test using Sign In button")
@allure.feature("Sign In")
@allure.story("Positive sign in test using Sign In button")
def test_sign_in(driver, sing_in_page, dash_page, main_page, user):
    # sing_in_page = SignInPage(driver)
    # user = User(username="admin", password="pass")
    # assert main_page.is_element_present(InternalPageLocators.SIGN_IN)
    main_page.sign_in_menu.click()
    assert sing_in_page.sign_in_button.get_attribute("value") == "Sign In"
    sing_in_page.input_username(user.username)
    sing_in_page.input_password(user.password)
    sing_in_page.press_sign_in()
    # dash_page = DashboardPage(driver)
    assert dash_page.title() == "Oxwall - Find New Friends Here!"


@allure.title("Sign in test using submit")
@allure.feature("Sign In")
@allure.story("Positive sign in test using submit")
def test_sign_in_submit(driver, sing_in_page, dash_page):
    # sing_in_page = SignInPage(driver)
    user = User(username="demo", password="demo")
    sing_in_page.input_username(user.username)
    sing_in_page.input_password(user.password)
    sing_in_page.submit()
    # dash_page = DashboardPage(driver)
    assert dash_page.title() == "Pieter - social networking"


@allure.title("Sign in test without password")
@allure.feature("Sign In")
@allure.story("Negative sign in test: without password")
def test_sign_in_without_password(driver, sing_in_page, dash_page):
    # sing_in_page = SignInPage(driver)
    user = User(username="demo", password="demo")
    sing_in_page.input_username(user.username)
    sing_in_page.submit()
    assert sing_in_page.driver.title == "Sign in to Pieter - Find Friends Here!"


@allure.title("Sign in test wrong password")
@allure.feature("Sign In")
@allure.story("Negative sign in test: wrong password")
def test_sign_in_wrong_password(driver, sing_in_page, dash_page):
    # sing_in_page = SignInPage(driver)
    user_with_wrong_pass = User(username="demo", password="pass")

    sing_in_page.input_username(user_with_wrong_pass.username)
    sing_in_page.input_password(user_with_wrong_pass.password)
    sing_in_page.submit()
    assert sing_in_page.driver.title == "Sign in to Pieter - Find Friends Here!"
