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
# import config
#
# config.BASE_URL

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json",
                     help="project config file name")
    # parser.addoption("--browser", action="store", default="Chrome",
    #                  help="driver")


@pytest.fixture(scope="session")
def config(request):
    filename = request.config.getoption("--config")
    with open(os.path.join(PROJECT_PATH, filename)) as f:
        return json.load(f)


@pytest.fixture()
def driver(config, selenium, base_url):
    # browser = request.config.getoption("--browser")
    # if browser.lower() == "chrome":
    #     driver = webdriver.Chrome()
    # elif browser.lower() == "firefox":
    #     driver = webdriver.Firefox()
    driver = selenium
    driver.get(base_url)                 #   "https://demo.oxwall.com/")
    yield driver
    driver.close()


@pytest.fixture()
def db(config):
    db = DB(**config["db"])
    yield db
    db.close()


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
def sign_in_user(driver, main_page, sing_in_page, config):
    # Login
    user = User(**config["web"]["admin_user"])
    main_page.open_sign_in_form()
    sing_in_page.sign_in(user)
    sing_in_page.wait_next_page()
    yield user
    main_page.sign_out()  # TODO: fix sign out
