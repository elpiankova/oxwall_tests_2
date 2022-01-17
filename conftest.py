import json
import os.path

import pytest
from selenium import webdriver

from app import OxwallApp
from db.db_connector import DB
from pages.dashboard_page import DashboardPage
from pages.main_page import MainPage
from pages.signin_page import SignInPage
from value_objects.user import User


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall/")                 #   "https://demo.oxwall.com/")
    yield driver
    driver.close()


@pytest.fixture()
def db():
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "mysql",
        "db": "oxwall1"
    }
    db = DB(**db_config)
    yield db
    db.close()


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(PROJECT_PATH, "data", "users.json"), encoding="utf8") as f:
    user_list = [User(**u) for u in json.load(f)]


@pytest.fixture(params=user_list, ids=[repr(u) for u in user_list])
def user(db, request):
    user = request.param
    db.create_user(user)

    # def final():
    #     db.delete_user(user)
    # request.addfinalizer(final)
    yield user
    db.delete_user(user)


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
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def sign_in_user(driver, main_page, sing_in_page):
    # Login
    user = User(username="admin", password="pass", real_name="Admin")
    main_page.open_sign_in_form()
    sing_in_page.sign_in(user)
    # TODO wait Dashboard page
    yield user
    # main_page.logout()  # TODO: sign out
