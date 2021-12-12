def presence_of_elements_located_by_number(locator, number):

    def _predicate(driver):
        elements = driver.find_elements(*locator)
        if len(elements) == number:
            return elements

    return _predicate


# class presence_of_elements_located_by_number:
#     def __init__(self, locator, number):
#         self.locator = locator
#         self.number = number
#
#     def __call__(self, driver):
#         elements = driver.find_elements(*self.locator)
#         if len(elements) == self.number:
#             return elements

# class A:
#     def __init__(self, x):
#         self.x = x
#
#     def __call__(self, other):
#         return self.x ** other
#
#
# a = A(10)
# b = A(2)
# # print(a + 1)
# print(a(32))
# print(a(50))
# print(b(32))



