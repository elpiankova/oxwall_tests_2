from selenium.webdriver.support import expected_conditions as ec

from pages.elements.post_block import PostBlock


class ElementObject:
    def __init__(self, locator):
        self.locator = locator

    def __get__(self, obj, owner):
        el = obj.wait.until(ec.presence_of_element_located(self.locator),
                            message=f"No element with locator='{self.locator}'")
        return el


class ElementsObject:
    def __init__(self, locator):
        self.locator = locator

    def __get__(self, obj, owner):
        els = obj.wait.until(ec.presence_of_all_elements_located(self.locator),
                             message=f"No element with locator='{self.locator}'")
        return els



