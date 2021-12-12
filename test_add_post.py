from selenium.webdriver.common.by import By


def test_add_post(driver, dash_page, sign_in):
    # TODO parametrize input_text
    input_text = "test1223"

    old_number_of_post = dash_page.count_posts()
    dash_page.create_new_text_post(input_text)
    new_list_of_posts = dash_page.wait_new_post(old_number_of_post)

    # Verify text of new post
    # TODO we will change this line soon:
    post_text = new_list_of_posts[0].find_element(By.CLASS_NAME, "ow_newsfeed_content ")
    assert post_text.text == input_text
