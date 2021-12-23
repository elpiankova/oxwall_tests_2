import pytest
from selenium import webdriver

from app import OxwallApp
from pages.dashboard_page import DashboardPage
from pages.signin_page import SignInPage
from value_objects.user import User


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.oxwall.com/")
    yield driver
    driver.close()


# @pytest.fixture()
# def app(driver):
#     return OxwallApp(driver)

@pytest.fixture()
def sing_in_page(driver):
    return SignInPage(driver)


@pytest.fixture()
def dash_page(driver):
    return DashboardPage(driver)


@pytest.fixture()
def sign_in_user(driver, sing_in_page):
    # Login
    user = User(username="demo", password="demo", real_name="Demo")
    sing_in_page.sign_in(user)
    # TODO wait Dashboard page
    yield user
    # TODO: sign out
