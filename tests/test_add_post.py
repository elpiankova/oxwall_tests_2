import os.path
import time
import json

import allure
import pytest

from conftest import PROJECT_PATH
from data.random_string import random_string

with open(os.path.join(PROJECT_PATH, "data", "post_text.json")) as f:
    data_list = json.load(f)

data_list.append(random_string())
data_list[0] = pytest.param(data_list[0], marks=pytest.mark.smoke, id=data_list[0])


@allure.title("Post create test")
@allure.feature("Post")
@allure.story("Create text post (without photos)")
@pytest.mark.smoke
# @pytest.mark.xfail
# @pytest.mark.nondestructive
@pytest.mark.parametrize("input_text", data_list)
def test_add_post(driver, dash_page, sign_in_user, input_text, db):
    old_number_of_post = dash_page.count_posts()
    dash_page.create_new_text_post(input_text)
    dash_page.wait_new_post(old_number_of_post)
    new_list_of_posts = dash_page.posts
    assert db.get_last_text_post() == input_text
    with allure.step(f'THEN this post block has this {input_text} and author as this user and time "within 1 minute"'):
        post = new_list_of_posts[0]
        assert post.text.replace("\r", "") == input_text.replace("\r", "")
        assert post.user == sign_in_user
        assert post.time_created == "within 1 minute"


@allure.title("Add like test")
@allure.feature("Post")
@allure.story("Add like to post")
def test_add_like(driver, dash_page, sign_in_user):
    time.sleep(2)
    posts = dash_page.posts
    print(posts[0].text)
    posts[0].add_like()
    assert posts[0].likes_count() == 12
