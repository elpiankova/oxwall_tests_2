from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from custom_expected_condidion import presence_of_elements_located_by_number


def test_add_post():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 3, poll_frequency=0.1)

    driver.get("https://demo.oxwall.com/")

    login_elem = driver.find_element(By.NAME, "identity")
    login_elem.clear()
    login_elem.send_keys("demo")

    pass_elem = driver.find_element(By.NAME, "password")
    pass_elem.clear()
    pass_elem.send_keys("demo")

    sign_in_button = driver.find_element(By.NAME, "submit")
    sign_in_button.click()

    # new_post_elem = driver.find_element(By.NAME, "status")
    new_post_elem = wait.until(ec.presence_of_element_located((By.NAME, "status")),
                               message="Can't find new post text area")

    posts = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
    old_number_of_post = len(posts)

    new_post_elem.click()
    new_post_elem.send_keys("test")

    send_button = driver.find_element(By.NAME, "save")
    send_button.click()

    new_number = old_number_of_post + 1

    posts = wait.until(presence_of_elements_located_by_number((By.CLASS_NAME, "ow_newsfeed_item"), new_number + 1),
                       message=f"Not find {new_number} post elements")

    driver.close()
