

def test_sign_in(driver, sing_in_page, dash_page):
    # sing_in_page = SignInPage(driver)
    user = {"username": "demo", "password": "demo"}

    sing_in_page.input_username(user['username'])
    sing_in_page.input_password(user['password'])
    sing_in_page.press_sign_in()
    # dash_page = DashboardPage(driver)
    assert dash_page.title() == "Pieter - social networking"


def test_sign_in_submit(driver, sing_in_page, dash_page):
    # sing_in_page = SignInPage(driver)
    user = {"username": "demo", "password": "demo"}
    sing_in_page.input_username(user['username'])
    sing_in_page.input_password(user['password'])
    sing_in_page.submit()
    # dash_page = DashboardPage(driver)
    assert dash_page.title() == "Pieter - social networking"


def test_sign_in_without_password(driver, sing_in_page, dash_page):
    # sing_in_page = SignInPage(driver)
    user = {"username": "demo", "password": "demo"}
    sing_in_page.input_username(user['username'])
    sing_in_page.submit()
    assert sing_in_page.driver.title == "Sign in to Pieter - Find Friends Here!"


def test_sign_in_wrong_password(driver, sing_in_page, dash_page):
    # sing_in_page = SignInPage(driver)
    user_with_wrong_pass = {"username": "demo", "password": "pass"}

    sing_in_page.input_username(user_with_wrong_pass['username'])
    sing_in_page.input_password(user_with_wrong_pass['password'])
    sing_in_page.submit()
    assert sing_in_page.driver.title == "Sign in to Pieter - Find Friends Here!"