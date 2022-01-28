from pytest_bdd import given, when, then, scenario, parsers

from value_objects.user import User


@scenario("posts.feature", "Create text post (without photos)")
def test_add_post():
    pass


@given("initial amount of post in Oxwall database", target_fixture="initial_posts")
def initial_posts(dash_page):
    return len(dash_page.posts)


@given("I as a logged user", target_fixture="logged_user")
def logged_user(config, main_page, sing_in_page):
    user = User(**config["web"]["admin_user"])
    main_page.open_sign_in_form()
    sing_in_page.sign_in(user)
    return user
    # main_page.logout()


@when(parsers.parse("I add a new post with {text} in Dashboard page"))
def create_post(dash_page, text):
    dash_page.create_new_text_post(text)


@then("a new post block appears before old table of posts")
def wait_new_post(dash_page, initial_posts):
    dash_page.wait_new_post(initial_posts)


@then(parsers.parse("this post block has this {text} and author as this user and time \"within 1 minute\""))
def verify_new_post(dash_page, text, logged_user):
    new_list_of_posts = dash_page.posts
    post = new_list_of_posts[0]
    assert post.text == text
    assert post.user == logged_user
    assert post.time_created == "within 1 minute"
