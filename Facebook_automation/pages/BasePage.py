
# all the libraries that we need for automation and testing
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp

"""This class is the parent class of all pages
It contains all the common methods and utilities for other page classes"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    """this method deals with clicking operation for any element"""
    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(exp.visibility_of_element_located(locator)).click()

    """This method is used for sending information to the website"""
    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(exp.visibility_of_element_located(locator)).send_keys(text)

    """This method returns the title of the page"""
    def get_element_title(self, locator):
        element = WebDriverWait(self.driver, 10).until(exp.visibility_of_element_located(locator))
        return element.text

    """this method confirms whether a elements is visible or not"""
    def is_enabled(self, locator):
        element = WebDriverWait(self.driver, 10).until(exp.visibility_of_element_located(locator))
        return bool(element)
